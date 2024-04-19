import os
import random
import shutil
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.learning_area.utils import process_time


COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
USER_INFO = os.path.join('structure', 'Server', 'cust', 'user_info')
# PATH = os.path.join('C:\\', 'Users', 'admin', 'Desktop', 'structure', 'Server', 'cust', 'user_info') # 所有的用戶到這邊的路徑都一樣
COMPUTER_USER_INFO_PATH = os.path.join(COMPUTER_DESK, USER_INFO)
NOTEBOOK_USER_INFO_PATH = os.path.join(NOTEBOOK_DESK, USER_INFO)

# 學習區的路徑
LEARNING = os.path.join('email#1', 'learning') # 根據用戶所註冊的email來修改email#1, 也就是email#1要是動態的
LEARNING_COMPUTER_PATH = os.path.join(COMPUTER_USER_INFO_PATH, LEARNING) # 到達此用戶學習區用來放置各個影片的筆記空間 -> 一個url對應一個資料夾
LEARNING_NOTEBOOK_PATH = os.path.join(NOTEBOOK_USER_INFO_PATH, LEARNING)

# 習題區的路徑
INDIVIDUAL_EXERCISE_ANSWER_AREA = os.path.join('email#1', 'note', 'exercise_answer') # email#1替換成個別用戶註冊的信箱, 就是個別用戶的專屬路徑了
EXERCISE_ANSWER_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, INDIVIDUAL_EXERCISE_ANSWER_AREA)

# 自定義區的路徑
SELF_DEFINED_PATH = os.path.join('email#1', 'note', 'self_defined')
SELF_DEFINED_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, SELF_DEFINED_PATH)

# 播放清單的路徑
PLAYLIST_PATH = os.path.join('email#1', 'playlist')
PLAYLIST_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, PLAYLIST_PATH)

# 科目英文名轉中文名的映射
ENG_TO_CH = {
    'calculus': '微積分',
    'linear_algebra': '線性代數',
    'general_physics': '普通物理',
    'data_structure': '資料結構',
}
# 中文轉英文的映射
CH_TO_ENG ={v:k for k, v in ENG_TO_CH.items()}

@csrf_exempt
def note(request):
    if request.method == 'GET':
        return render(request, 'note.html')
    
    if request.POST['purpose'] == 'showMore':
        if request.POST['id'] == 'learningAreaCourseMore': 
            # 要獲取學習影片區課名
            learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
            course_list = list(set([file_name.split('[]')[1] for file_name in learning_full_folder_name_list])) # 每一個元素都不重複, 所以做這些轉換
            context = {
                'status': True,
                'data': course_list,
            }
            return JsonResponse(context)
        elif request.POST['id'] == 'learningAreaLecturerMore':
            # 要獲取學習影片區授課者
            learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
            lecturer_list = list(set([file_name.split('[]')[0] for file_name in learning_full_folder_name_list])) # 每一個元素都不重複, 所以做這些轉換
            context = {
                'status': True,
                'data': lecturer_list,
            }
            return JsonResponse(context)
        else:
            # 習題答案區的按鈕
            exercise_answer_subject_list = os.listdir(EXERCISE_ANSWER_AREA_PATH)
            subject_list = [ENG_TO_CH[subject] for subject in exercise_answer_subject_list]
            context = {
                'status': True,
                'data': subject_list,
            }
            return JsonResponse(context)
        
    if request.POST['purpose'] == 'mainPageBtn':
        # 學習影片區
        learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
        choices = random.sample(learning_full_folder_name_list, 2)
        course_list = list(set([file_name.split('[]')[1] for file_name in choices]))
        lecturer_list = list(set([file_name.split('[]')[0] for file_name in choices])) 
        
        # 習題答案區
        exercise_answer_folder_list = os.listdir(EXERCISE_ANSWER_AREA_PATH)
        exercise_choices = random.sample(exercise_answer_folder_list, 2)
        exercise_list = [ENG_TO_CH[subject] for subject in exercise_choices]
        
        context = {
            'status': True,
            'data': {
                'course_list': course_list,
                'lecturer_list': lecturer_list,
                'exercise_list': exercise_list,
                
            }
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'renameLearning':
        from_course = request.POST.get('fromCourse')
        if from_course == 'false':
            from_course = False
        old_name = request.POST.get('oldName', '')
        new_name = request.POST.get('newName', '')
        learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
        if from_course:
            for folder_name in learning_full_folder_name_list:
                if old_name in folder_name.split('[]')[1]:
                    old_path = os.path.join(LEARNING_COMPUTER_PATH, folder_name)
                    new_folder_name = folder_name.replace(old_name, new_name, 1)
                    new_path = os.path.join(LEARNING_COMPUTER_PATH, new_folder_name)
                    os.rename(old_path, new_path)
                    # 因為要把整排含有舊有名字的檔案全部重新命名, 所以整個for迴圈要跑完
            context = {
                'status': True,
                'data': '重新命名成功!',
            }
            return JsonResponse(context)

        for folder_name in learning_full_folder_name_list:
            if old_name in folder_name.split('[]')[0]:
                old_path = os.path.join(LEARNING_COMPUTER_PATH, folder_name)
                new_folder_name = folder_name.replace(old_name, new_name, 1)
                new_path = os.path.join(LEARNING_COMPUTER_PATH, new_folder_name)
                os.rename(old_path, new_path)
                # 因為要把整排含有舊有名字的檔案全部重新命名, 所以整個for迴圈要跑完
        context = {
            'status': True,
            'data': '重新命名成功!',
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'renameSelfDefined':
        old_name = request.POST.get('oldName', '')
        new_name = request.POST.get('newName', '')
        path_list = request.POST.get('path', '').split(' > ')
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *path_list)
        full_items_list = os.listdir(exact_path)
        for item_name in full_items_list:
            if old_name == item_name:
                old_path = os.path.join(exact_path, item_name)
                new_path = os.path.join(exact_path, new_name)
                os.rename(old_path, new_path)
                # 因為只會有一個檔案要重名, 所以可以在這裡return
                context = {
                    'status': True,
                    'data': '重新命名成功!',
                }
                return JsonResponse(context)
        context = {
            'status': False,
            'error': '重新命名失敗: 找不到此檔案'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'playlistRename':
        old_name = request.POST.get('oldName', '')
        new_name = request.POST.get('newName', '')
        playlist_list = os.listdir(PLAYLIST_AREA_PATH)
        for playlist_name in playlist_list:
            if old_name == playlist_name:
                old_path = os.path.join(PLAYLIST_AREA_PATH, old_name)
                new_path = os.path.join(PLAYLIST_AREA_PATH, new_name)
                os.rename(old_path, new_path)
                # 因為只會有一個檔案要重名, 所以可以在這裡return
                context = {
                    'status': True,
                    'data': '重新命名成功!',
                }
                return JsonResponse(context)
        context = {
            'status': False,
            'error': '重新命名失敗: 找不到此檔案'
        }
        return JsonResponse(context)
        
    if request.POST['purpose'] == 'deleteSelfDefined':
        is_folder = request.POST.get('isFolder', '')
        is_folder = True if is_folder == 'true' else False
        name = request.POST.get('name', '')
        path_list = request.POST.get('path', '').split(' > ')
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *path_list, name)
        if os.path.exists(exact_path):
            if is_folder:
                shutil.rmtree(exact_path)
                context = {
                    'status': True,
                    'data': f'成功刪除"{name}" 資料夾'
                }
                return JsonResponse(context)
            
            os.remove(exact_path)
            context = {
                'status': True,
                'data': f'成功刪除"{name}" 筆記板'
            }
            return JsonResponse(context)
        
        context = {
                'status': False,
                'error': f'刪除失敗: 找不到"{name}"'
            }
        return JsonResponse(context)
      
    if request.POST['purpose'] == 'playlistDelete':
        name = request.POST.get('name', '')
        exact_path = os.path.join(PLAYLIST_AREA_PATH, name)
        if os.path.exists(exact_path):
            shutil.rmtree(exact_path)
            context = {
                'status': True,
                'data': f'成功刪除"{name}" 資料夾'
            }
            return JsonResponse(context)
        
        context = {
                'status': False,
                'error': f'刪除失敗: 找不到"{name}"'
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'playlistVideoDelete':
        playlist_title = request.POST.get('playlistTitle', '')
        video_title = request.POST.get('videoTitle', '')
        playlist_path = os.path.join(PLAYLIST_AREA_PATH, playlist_title)
        video_list = os.listdir(playlist_path)
        for video_name in video_list:
            if video_title in video_name:
                video_path = os.path.join(playlist_path, video_name)
                if os.path.exists(video_path):
                    os.remove(video_path)
                    context = {
                        'status': True,
                        'data': f'成功自{playlist_title}移除"{video_title}"'
                    }
                    return JsonResponse(context)
        
        context = {
                'status': False,
                'error': f'刪除失敗: "{video_title}"不存在'
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showLearningAreaData':
        course_filter_text = request.POST.get('courseFilterText', '')
        lecturer_filter_text = request.POST.get('lecturerFilterText', '')
        learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
        data_list = []
        
        if course_filter_text:
            for folder_name in learning_full_folder_name_list:
                if course_filter_text in folder_name.split('[]')[1]:
                    data_list.append(folder_name.split('[]'))

            context = {
                'status': True,
                'data': data_list,
            }
            return JsonResponse(context)
        if lecturer_filter_text:
            for folder_name in learning_full_folder_name_list:
                if lecturer_filter_text in folder_name.split('[]')[0]:
                    data_list.append(folder_name.split('[]'))

            context = {
                'status': True,
                'data': data_list,
            }
            return JsonResponse(context)
    
    if request.POST['purpose'] == 'showExerciseAreaData':
        chinese_subject = request.POST.get('chineseSubject', '')
        subject = CH_TO_ENG[chinese_subject]
        subject_path = os.path.join(EXERCISE_ANSWER_AREA_PATH, subject)
        if os.path.exists(subject_path):
            panel_list = os.listdir(subject_path)
            context = {
                'status': True,
                'data': {'panel_list': panel_list,
                         'subject': subject,}
            }
            return JsonResponse(context)
        
        context = {
            'status': False,
            'error': '該科目路徑不存在'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'notePanelTags':
        video_id = request.POST.get('videoId', '')
        learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
        video_notes_path = ''
        for folder_name in learning_full_folder_name_list:
            if video_id in folder_name:
                video_notes_path = os.path.join(LEARNING_COMPUTER_PATH, folder_name)
                break
        panels_list = [panel_name.replace(';', ':') for panel_name in os.listdir(video_notes_path)]
        
        start_end_dict = {}
        for panel in panels_list:
                # start_end_dict的 key是檔案名, value是字典, 字典內容為起始跟終止的秒數, 如下所示.
                time, description = panel.split('-')
                start, end = time.split('~')
                start = process_time.total_seconds(start)
                end = process_time.total_seconds(end)
                start_end_dict[time + '-' + description] = {'start':start, 'end': end}
        context = {
            'status': True,
            'data': start_end_dict,
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showingNotePanel':
        video_id = request.POST.get('videoId', '')
        panel_name = request.POST.get('panelName', '').replace(':', ';')
        panel_file_path = ''
        learning_full_folder_name_list = os.listdir(LEARNING_COMPUTER_PATH)
        for folder_name in learning_full_folder_name_list:
            if video_id in folder_name:
                panel_file_path = os.path.join(LEARNING_COMPUTER_PATH, folder_name, panel_name)
                break
        context = {
            'status': True,
            'data': panel_file_path,
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showingAnswerPanel':
        subject = request.POST.get('subject', '')
        name = request.POST.get('panelName', '')
        panel_name = name.replace('-', '[]')
        panel_file_path = os.path.join(EXERCISE_ANSWER_AREA_PATH, subject, panel_name)
        if os.path.exists(panel_file_path):
            context = {
                'status': True,
                'data': panel_file_path,
            }
            return JsonResponse(context)
        
        context = {
            'status': False,
            'error': f'"{name}"筆記板不存在'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'selfDefinedPanel':
        path_list = request.POST.get('path', '').split(' > ')
        panel_name = request.POST.get('panelName', '')
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *path_list, panel_name)
        if os.path.exists(exact_path):
            context = {
                'status': True,
                'data':exact_path,
            }
            return JsonResponse(context)
        
        context = {
            'status': False,
            'error': f'"{panel_name}"筆記板不存在'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showSelfDefinedModal':
        path_list = request.POST.get('path', '').split(' > ')
        folder_name = request.POST.get('folderName', '')
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *path_list, folder_name)
        folder_list = [name for name in os.listdir(exact_path) if not name.endswith('.txt')]
        panel_list = [name for name in os.listdir(exact_path) if name.endswith('.txt')]
        context = {
            'status': True,
            'data': {
                'folder_list': folder_list,
                'panel_list': panel_list,
            }
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'addSelfDefined':
        is_folder = request.POST.get('isFolder', '')
        is_folder = True if is_folder == 'true' else False
        name = request.POST.get('name', '')
        path_list = request.POST.get('path', '').split(' > ')
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *path_list, name)
        if is_folder:
            os.makedirs(exact_path)
            context = {'status': True}
            return JsonResponse(context)
        
        with open(exact_path, 'w'):
            pass
        context = {'status': True}
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showPlaylistModal':
        playlist_list = os.listdir(PLAYLIST_AREA_PATH)
        context = {'status': True, 'data': playlist_list}
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'showPlaylistVideoModal':
        playlist_name = request.POST.get('playlistName', '')
        exact_path = os.path.join(PLAYLIST_AREA_PATH, playlist_name)
        video_info_dict = {}
        if os.path.exists(exact_path):
            video_list = os.listdir(exact_path)
            for item in video_list:
                video_title, video_id = os.path.splitext(item)[0].split('[]')
                video_info_dict[video_id] = video_title
            context = {'status': True, 'data': video_info_dict}
            return JsonResponse(context)
        
        context = {'status': False, 'error': f'"{playlist_name}"不存在'}
        return JsonResponse(context)