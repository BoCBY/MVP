import os
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.exercise_area.utils import pdf

EXERCISE = os.path.join('structure', 'Server', 'non_cust', 'exercise')
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
COMPUTER_EXERCISE_PATH = os.path.join(COMPUTER_DESK, EXERCISE)
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
NOTEBOOK_EXERCISE_PATH = os.path.join(NOTEBOOK_DESK, EXERCISE)

@csrf_exempt
def exercise(request):
    if request.method == 'GET':
        return render(request, 'exercise.html')
    
    if request.POST['purpose'] == 'oneBtn':
        subject = request.POST.get('SUBJECT', '')
        pdf_path = pdf.create_questions_pdf(subject, True) # 在一鍵生成的資料夾中生成試題檔案
        
        if os.path.exists(pdf_path):
            context = {
                'status': True,
                'pdf_path': pdf_path,
            }
            return JsonResponse(context)
        context = {
            'status': False,
            'error': 'PDF file not found'
        }
        return JsonResponse(context)
        
    if request.POST['purpose'] == 'regularQuestion':
        subject = request.POST.get('subject', '')
        date = request.POST.get('date', '')
        file_name = request.POST.get('fileName', '')
        period = request.POST.get('period', '')
        file_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, period, date, file_name)
    
        if os.path.exists(file_path):
            context = {
                'status': True,
                'file_path': file_path,
            }
            return JsonResponse(context)
        context = {
            'status': False,
            'error': 'PDF file not found'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'regularAnswer':
        subject = request.POST.get('subject', '')
        date = request.POST.get('date', '')
        number = request.POST.get('number', '')
        period = request.POST.get('period', '')
        file_name = request.POST.get('fileName', '')
        file_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, period, date, 'answer', number, file_name)
    
        if os.path.exists(file_path):
            context = {
                'status': True,
                'file_path': file_path,
            }
            return JsonResponse(context)
        context = {
            'status': False,
            'error': 'PDF file not found'
        }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'makeTags':
        subject = request.POST.get('subject', '')
        present_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, 'present')
        past_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, 'past')
        inside_present = os.listdir(present_path)
        inside_past = os.listdir(past_path)
        if os.path.exists(present_path) and os.path.exists(past_path):
            context = {
                'status': True,
                'present': inside_present,
                'past': inside_past,
            }
            return JsonResponse(context)
        
        context = {
                'status': False,
                'error': 'present or past folder does NOT exist.'
            }
        return JsonResponse(context)
    
    if request.POST['purpose'] == 'openQuestionNumModal':
        subject = request.POST.get('subject', '')
        date = request.POST.get('date', '')
        number = request.POST.get('number', '')
        period = request.POST.get('period', '')
        folder_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, period, date, 'answer', number)
        file_dict = {}
        if os.path.exists(folder_path):
            file_list = os.listdir(folder_path)
            for file_name in file_list:
                if file_name.endswith('.txt'): # 之後有筆記板就要改成筆記板檔案的副檔名
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r') as file:
                        like_line = file.readline().strip()
                        dislike_line = file.readline().strip()
                        like = int(like_line.split(': ')[1])
                        dislike = int(dislike_line.split(': ')[1])
                        file_dict[file_name] = {'like': like, 'dislike': dislike}
            context = {
                'status': True,
                'file_dict': file_dict,
            }
            return JsonResponse(context)
        
        context = {
                'status': False,
                'error': '該資料夾不存在',
            }
        return JsonResponse(context)
        

    
    
    
    
    
    