import os
from django.http import JsonResponse
from apps.learning_area import models
from django.views.decorators.csrf import csrf_exempt
from apps.learning_area.utils import url_conversion, forms, path, process_time, yt_video_info, bili_video_info
from django.shortcuts import render, redirect, HttpResponse

COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
USER_INFO = os.path.join('structure', 'Server', 'cust', 'user_info')
# PATH = os.path.join('C:\\', 'Users', 'admin', 'Desktop', 'structure', 'Server', 'cust', 'user_info') # 所有的用戶到這邊的路徑都一樣
COMPUTER_USER_INFO_PATH = os.path.join(COMPUTER_DESK, USER_INFO)
NOTEBOOK_USER_INFO_PATH = os.path.join(NOTEBOOK_DESK, USER_INFO)

LEARNING = os.path.join('email#1', 'learning') # 根據用戶所註冊的email來修改email#1, 也就是email#1要是動態的
LEARNING_COMPUTER_PATH = os.path.join(COMPUTER_USER_INFO_PATH, LEARNING) # 到達此用戶學習區用來放置各個影片的筆記空間 -> 一個url對應一個資料夾
LEARNING_NOTEBOOK_PATH = os.path.join(NOTEBOOK_USER_INFO_PATH, LEARNING)

PLAYLIST = os.path.join('email#1', 'playlist')
PLAYLIST_PATH = os.path.join(COMPUTER_USER_INFO_PATH, PLAYLIST)
@csrf_exempt
def learning(request): 
    if request.method == 'GET':
        film_form = forms.FilmModelForm()
        description_form = forms.Description() 
        context = {
            'film_form': film_form,
            'description_form': description_form,
            } 
        return render(request, 'learning.html', context)
    
    if 'url' in request.POST:
    # 獲取使用者要觀看的影片基本資訊(接收ajax請求)
        # 在筆記區要開啟選擇的影片至學習區開啟
        if request.POST.get('purpose') == 'newTab': 
            lecturer = request.POST.get('lecturer', '')
            course = request.POST.get('course', '')
            url = request.POST.get('url', '')
            video_id = request.POST.get('videoId') # yt影片的video id是11碼, bilibili是12碼, 如果又來自播放清單的影片的話, 那就是video id(12個字元)+?p=(集數)
            if len(video_id) == 11: #YT影片
                title, duration = yt_video_info.title_and_duration(url)
                url = url_conversion.yt_conversion(url)
                
            else: #BILI影片, 
                title, duration = bili_video_info.title_and_duration(url)
                url = url_conversion.bili_conversion(url)
                
            
            # 創建或查看此url影片的資料夾
            folder_path = path.create_folder(lecturer, course, video_id)
            suffix_name_list = os.listdir(folder_path)
            name_list = [os.path.splitext(name)[0] for name in suffix_name_list]
            file_name_list = [name.replace(';', ':').split('-') for name in name_list]
            start_end_dict = {}              
            for time, description in file_name_list:
                # start_end_dict的 key是檔案名, value是字典, 字典內容為起始跟終止的秒數, 如下所示.
                start, end = time.split('~')
                start = process_time.total_seconds(start)
                end = process_time.total_seconds(end)
                start_end_dict[time + '-' + description] = {'start':start, 'end': end}
            
            context = {'status': True,
                    'lecturer': lecturer,
                    'course': course,
                    'url': url,
                    'start_end_dict': start_end_dict,
                    'title': title,
                    'duration': duration,
                    }
            return JsonResponse(context)
            
        form = forms.FilmModelForm(data=request.POST)
        if form.is_valid():
            # 用戶填寫正確, 就獲取填寫的內容
            lecturer = form.cleaned_data.get('lecturer')
            course = form.cleaned_data.get('course')
            url = form.cleaned_data.get('url')
            
            # 獲取影片名稱與影片時長
            original_url = request.POST.get('url', '')
            if 'bili' in original_url:
                title, duration = bili_video_info.title_and_duration(original_url)
            else:
                title, duration = yt_video_info.title_and_duration(original_url)
            
            
            # 創建或查看此url影片的資料夾
            video_id = url_conversion.extract_video_id(url)
            folder_path = path.create_folder(lecturer, course, video_id)
            suffix_name_list = os.listdir(folder_path)
            name_list = [os.path.splitext(name)[0] for name in suffix_name_list]
            file_name_list = [name.replace(';', ':').split('-') for name in name_list]
            start_end_dict = {}              
            for time, description in file_name_list:
                # start_end_dict的 key是檔案名, value是字典, 字典內容為起始跟終止的秒數, 如下所示.
                start, end = time.split('~')
                start = process_time.total_seconds(start)
                end = process_time.total_seconds(end)
                start_end_dict[time + '-' + description] = {'start':start, 'end': end}
            
            context = {'status': True,
                    'lecturer': lecturer,
                    'course': course,
                    'url': url,
                    'start_end_dict': start_end_dict,
                    'title': title,
                    'duration': duration,
                    'video_id': video_id,
                    }
            
            
            return JsonResponse(context)
            
        context = {
            'status': False,
            'errors': form.errors
        }
        return JsonResponse(context)

    
    if 'description' in request.POST:
        # 獲取使用者輸入的時間段落描述(接收ajax請求)
        form = forms.Description(data=request.POST)
        if form.is_valid():
            # 用戶填寫正確, 就獲取填寫的內容
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')
            description = form.cleaned_data.get('description')
            start_time = process_time.total_seconds(start)
            end_time = process_time.total_seconds(end)
            video_duration = int(request.POST.get('videoDuration', ''))
            if end_time > video_duration:
                context = {'status': 'tooLong', 'error':'終止時間超過片長'}
                return JsonResponse(context)        
            
            # 進入當前頁面中url影片的資料夾
            film_url = request.POST.get('filmUrl')
            video_id = url_conversion.extract_video_id(film_url)
            folder_path = path.find_path(video_id)
            # 判斷使用者輸入的時段是否已存在
            for file_name in os.listdir(folder_path):
                if start + '~' + end in file_name:
                    context = {'status': 'duplicate',
                               'message': '相同時段筆記板已存在!'}
                    return JsonResponse(context)
            
            # 建立以時段+描述命名的檔案
            note_name = start + '~' + end + '-' + description + '.txt' # 先用文檔表示, 之後要用筆記板的副檔名
            path.make_files(folder_path, note_name)
            
            note_name_display = os.path.splitext(note_name.replace(';', ':'))[0].split('-') # 要傳到前端頁面展示的時段與段落描述的樣式
            
            
            data = { # 拿到時段檔案的名稱列表, 並傳送到後台
                'note_name_display': note_name_display,
                'start_time': start_time,
                'end_time': end_time,
            }
            context = {
                'status': True,
                'data': data,          
            }
            
            return JsonResponse(context)
            
        context = {
            'status': False,
            'errors': form.errors
        }
        return JsonResponse(context)
    
    if 'DELETE_ITEM[start]' in request.POST: # 來自deletePanel發送過來的ajax請求, 試了一下在request.POST的KEY就是這樣
        # 刪除指定的筆記板
        #print(request.POST)
        #print(request.POST['DELETE_ITEM[url]'])
        url = request.POST['DELETE_ITEM[url]']
        start = int(request.POST['DELETE_ITEM[start]'])
        end = int(request.POST['DELETE_ITEM[end]'])
        video_id = url_conversion.extract_video_id(url)
        folder_path = path.find_path(video_id) # 進到當前影片資料夾
        start_time_format = process_time.format_seconds(start).replace(':', ';')
        end_time_format = process_time.format_seconds(end).replace(':', ';')
        file_time_format = start_time_format + '~' + end_time_format # 可以找到要刪除的檔案
        file_name_list = os.listdir(folder_path)
        
        file_deleted = False
        deleted_file_name = None
        for file_name in file_name_list:
            if file_time_format in file_name:
                deleted_file_name = os.path.splitext(file_name)[0]
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
                file_deleted = True
                break
        
        if file_deleted:
            context = {
                'status': True,
                'start': request.POST['DELETE_ITEM[start]'],
                'end': request.POST['DELETE_ITEM[end]'],
                'deleted_file_name': deleted_file_name,
                }
            return JsonResponse(context)
        
        context = {
            'status': False,
            'error': '檔案不存在或已刪除',
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'savePlaylist':
        playlist_list = os.listdir(PLAYLIST_PATH)
        context = {
            'status': True,
            'data': playlist_list
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'addToNewPlaylist':
        invalid_to_valid = {
            '?': '？',
            '>': '＞',
            '<': '＜',
            '/': '／',
            '\\': '＼',
            '|': '｜',
            '"': '＂',
            '*': '＊',
            ':': '：',
        }
        playlist_name = request.POST.get('name', '')
        video_id = request.POST.get('videoId', '')
        video_title = request.POST.get('videoTitle', '')
        video_title_cleaned = ''.join(invalid_to_valid.get(char, char) for char in video_title)
        new_playlist_path = os.path.join(PLAYLIST_PATH, playlist_name)
        os.makedirs(new_playlist_path)
        # 要在這個資料夾裡儲存檔案
        exact_name = video_title_cleaned + '[]' + video_id + '.txt'
        exact_path = os.path.join(new_playlist_path, exact_name)
        with open(exact_path, 'w'):
            pass 
        context = {'status': True}
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'addToPlaylist':
        invalid_to_valid = {
            '?': '？',
            '>': '＞',
            '<': '＜',
            '/': '／',
            '\\': '＼',
            '|': '｜',
            '"': '＂',
            '*': '＊',
            ':': '：',
        }
        playlist_name = request.POST.get('playlistName', '')
        video_id = request.POST.get('videoId', '')
        video_title = request.POST.get('videoTitle', '')
        video_title_cleaned = ''.join(invalid_to_valid.get(char, char) for char in video_title)
        exact_name = video_title_cleaned + '[]' + video_id + '.txt'
        exact_path = os.path.join(PLAYLIST_PATH, playlist_name, exact_name)
        with open(exact_path, 'w'):
            pass 
        context = {'status': True}
        return JsonResponse(context)
        
    if request.POST['purpose'] == 'checkPlaylist':
        video_id = request.POST.get('videoId', '')
        dirs_containing_video = []
        
        for root, dirs, files in os.walk(PLAYLIST_PATH):
            if any(video_id in file for file in files):
                dirs_containing_video.append(os.path.basename(root))
                
        context = {
            'status': True,
            'data': dirs_containing_video,
        }
        return JsonResponse(context)
        