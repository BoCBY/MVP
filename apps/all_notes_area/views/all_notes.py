import os
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.all_notes_area.utils import cleaned_area_data

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
def all_notes(request):
    if request.method == 'GET':
        return render(request, 'all_notes.html')
    if request.POST['purpose'] == 'selectLearningArea':
        video_list = cleaned_area_data.clean_learning()
        context = {
            'status': True,
            'data': video_list,
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'selectExerciseAnswerArea':
        subject_list = cleaned_area_data.clean_exercise_answer()
        context = {
            'status': True,
            'data': subject_list,
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'selectSelfDefinedArea':
        location_list = cleaned_area_data.clean_self_defined()
        context = {
            'status': True,
            'data': location_list,
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'clickLearningNotePanel':
        directory_name = request.POST.get('directoryName', '')
        panel_name = request.POST.get('panelName', '').replace(':', ';', 4) + '.txt'
        exact_path = os.path.join(LEARNING_COMPUTER_PATH, directory_name, panel_name)
        if os.path.exists(exact_path):
            context = {
                'status': True,
                'data': exact_path,
            }
            return JsonResponse(context)
        context ={
            'status': False,
            'error': '此筆記板不存在'
        }
        return JsonResponse(context)
        
    if request.POST['purpose'] == 'clickExerciseAnswerNotePanel':
        chinese_subject_name = request.POST.get('chineseSubject', '')
        directory_name = CH_TO_ENG[chinese_subject_name]
        panel_name = request.POST.get('panelName', '') + '.txt'
        exact_path = os.path.join(EXERCISE_ANSWER_AREA_PATH, directory_name, panel_name)
        if os.path.exists(exact_path):
            context = {
                'status': True,
                'data': exact_path,
            }
            return JsonResponse(context)
        context ={
            'status': False,
            'error': '此筆記板不存在'
        }
        return JsonResponse(context)
        
    if request.POST['purpose'] == 'clickSelfDefinedNotePanel':
        location = request.POST.get('location', '')
        relative_path_list = location.replace('首頁', '').split(' > ') 
        panel_name = request.POST.get('panelName', '') + '.txt'
        exact_path = os.path.join(SELF_DEFINED_AREA_PATH, *relative_path_list, panel_name)
        if os.path.exists(exact_path):
            context = {
                'status': True,
                'data': exact_path,
            }
            return JsonResponse(context)
        context ={
            'status': False,
            'error': '此筆記板不存在'
        }
        return JsonResponse(context)