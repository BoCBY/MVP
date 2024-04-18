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

# 自定義區的路徑
SELF_DEFINED_PATH = os.path.join('email#1', 'note', 'self_defined')
SELF_DEFINED_AREA_PATH = os.path.join(COMPUTER_USER_INFO_PATH, SELF_DEFINED_PATH)

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
    