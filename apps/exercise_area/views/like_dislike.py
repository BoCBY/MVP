import os
import random
from datetime import datetime
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse

EXERCISE = os.path.join('structure', 'Server', 'non_cust', 'exercise')
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
COMPUTER_EXERCISE_PATH = os.path.join(COMPUTER_DESK, EXERCISE)
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
NOTEBOOK_EXERCISE_PATH = os.path.join(NOTEBOOK_DESK, EXERCISE)

@csrf_exempt
def like_dislike(request):
    subject = request.POST.get('subject', '')
    date = request.POST.get('date', '')
    period = request.POST.get('period', '')
    number = request.POST.get('number', '')
    file_name = request.POST.get('fileName', '')
    file_path = os.path.join(NOTEBOOK_EXERCISE_PATH, subject, period, date, 'answer', number, file_name)
    
    # like數儲存在文件的第一行, dislike數則在第二行. (行數是有offset的)
    if request.POST['action'] == 'like+1':
        if os.path.exists(file_path):
            like_line_number = 0 
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            like_line = lines[like_line_number].strip()
            count = int(like_line.split(':')[1])
            count += 1
            lines[like_line_number] = f'like: {count}\n'
            
            with open(file_path, 'w') as f:
                f.writelines(lines)
            
            context ={
                'status': True,
                'message': 'like+1'
            }    
            return JsonResponse(context)
        context = {
            'status': False,
            'error': '該檔案不存在'
        }
        return JsonResponse(context)
            
    if request.POST['action'] == 'dislike+1':
        if os.path.exists(file_path):
            dislike_line_number = 1 
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            dislike_line = lines[dislike_line_number].strip()
            count = int(dislike_line.split(':')[1])
            count += 1
            lines[dislike_line_number] = f'dislike: {count}\n'
            
            with open(file_path, 'w') as f:
                f.writelines(lines)
            
            context ={
                'status': True,
                'message': 'dislike-1'
            }    
            return JsonResponse(context)
        context = {
            'status': False,
            'error': '該檔案不存在'
        }
        return JsonResponse(context)
    
    if request.POST['action'] == 'like-1':
        if os.path.exists(file_path):
            like_line_number = 0 
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            like_line = lines[like_line_number].strip()
            count = int(like_line.split(':')[1])
            count -= 1
            lines[like_line_number] = f'like: {count}\n'
            
            with open(file_path, 'w') as f:
                f.writelines(lines)
            
            context ={
                'status': True,
                'message': 'like-1'
            }    
            return JsonResponse(context)
        context = {
            'status': False,
            'error': '該檔案不存在'
        }
        return JsonResponse(context)
    
    if request.POST['action'] == 'dislike-1':
        if os.path.exists(file_path):
            dislike_line_number = 1 
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            dislike_line = lines[dislike_line_number].strip()
            count = int(dislike_line.split(':')[1])
            count -= 1
            lines[dislike_line_number] = f'dislike: {count}\n'
            
            with open(file_path, 'w') as f:
                f.writelines(lines)
            
            context ={
                'status': True,
                'message': 'dislike-1'
            }    
            return JsonResponse(context)
        context = {
            'status': False,
            'error': '該檔案不存在'
        }
        return JsonResponse(context)
        