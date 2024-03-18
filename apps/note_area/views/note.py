import os
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# 學習區的路徑
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
LEARNING = os.path.join('structure', 'Server', 'cust', 'user_info')
# PATH = os.path.join('C:\\', 'Users', 'admin', 'Desktop', 'structure', 'Server', 'cust', 'user_info') # 所有的用戶到這邊的路徑都一樣
COMPUTER_LEARNING_PATH = os.path.join(COMPUTER_DESK, LEARNING)
NOTEBOOK_LEARNING_PATH = os.path.join(NOTEBOOK_DESK, LEARNING)

USER_EMAIL = os.path.join('email#1', 'learning') # 根據用戶所註冊的email來修改email#1, 也就是email#1要是動態的
USER_COMPUTER_PATH = os.path.join(COMPUTER_LEARNING_PATH, USER_EMAIL) # 到達此用戶學習區用來放置各個影片的筆記空間 -> 一個url對應一個資料夾
USER_NOTEBOOK_PATH = os.path.join(NOTEBOOK_LEARNING_PATH, USER_EMAIL)

# 習題區的路徑


@csrf_exempt
def note(request):
    if request.method == 'GET':
        return render(request, 'note.html')
    
    if request.POST['purpose'] == 'showMore':
        if request.POST['id'] == 'learningAreaCourseMore': 
            # 要獲取課名
            full_file_name_list = [file for file in os.listdir(USER_COMPUTER_PATH) if not file.endswith('.txt')] # 這個路徑中的readMe如果都知道了就可以把該檔案刪掉, 也就可以不用判斷式而直接用listdir就好(可以省很多效能)
            course_list = list(set([file_name.split('[]')[1] for file_name in full_file_name_list])) # 每一個元素都不重複, 所以做這些轉換
            context = {
                'status': True,
                'data': course_list,
            }
            return JsonResponse(context)
        elif request.POST['id'] == 'learningAreaLecturerMore':
            # 要獲取授課者
            full_file_name_list = [file for file in os.listdir(USER_COMPUTER_PATH) if not file.endswith('.txt')] # 這個路徑中的readMe如果都知道了就可以把該檔案刪掉, 也就可以不用判斷式而直接用listdir就好(可以省很多效能)
            lecturer_list = list(set([file_name.split('[]')[0] for file_name in full_file_name_list])) # 每一個元素都不重複, 所以做這些轉換
            context = {
                'status': True,
                'data': lecturer_list,
            }
            return JsonResponse(context)