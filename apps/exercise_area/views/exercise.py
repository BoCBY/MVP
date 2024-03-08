import os
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from apps.exercise_area.utils import pdf

@csrf_exempt
def exercise(request):
    if request.method == 'GET':
        return render(request, 'exercise.html')
    
    if 'subject' in request.POST:
        subject = request.POST.get('subject', '')
        pdf_path = pdf.create_questions_pdf(subject, True) # 在一鍵生成的資料夾中生成試題檔案
        
        if os.path.exists(pdf_path):
            context = {
                'status': True,
                'pdf_path': pdf_path,
            }
            return JsonResponse(context)
        else:
            context = {
                'status': False,
                'error': 'PDF file not found'
            }
            return JsonResponse(context)
    


    
    
    
    
    
    