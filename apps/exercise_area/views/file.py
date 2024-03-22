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

'''在Django中
   從線上下載不同類型的檔案的code只有在content_type那裏會不一樣而已, 根據檔案的類型輸入對應的值就可以了
   至於在網路上呈現, 則是response['content-Disposition']的值不一樣而已, 'attachment'是下載; inline是線上看'''

def serve_pdf(request):
    '''給用戶下載試題檔案'''
    path = request.GET.get('path', '')
    if os.path.exists(path):
        if 'one_button'not in path:
            with open(path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response
          
        with open(path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(path)
        os.remove(path) # 把伺服器裡的一鍵生成檔案刪除, 定期的試題則保留
        return response      
    return HttpResponse("PDF file not found", status=404)

def download_answer_panel(request):
    '''給用戶下載筆記板檔案(暫時先用.txt呈現)'''
    path = request.GET.get('path', '')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            response = HttpResponse(file.read(), content_type='text/plain; charset=utf-8')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
        
        return response
    return HttpResponse("file not found", status=404)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        subject = request.POST.get('subject', '')
        date = request.POST.get('date', '')
        number = request.POST.get('number', '')
        period = request.POST.get('period', '')
        
        path = os.path.join(COMPUTER_EXERCISE_PATH, subject, period, date, 'answer', number)
        name_list = ['Jerry', 'Cora', 'KG', 'LBJ', 'KD', 'Curry', 'Wemby', 'Euler', 'Gauss', 'Newton', 'Einstein', 'Feymann', 'Dirac', 'Maxwell']
        id = random.sample(name_list, 1)[0]
        upload_time = datetime.now().strftime('%Y%m%d%H%M')
        file_name = id + '-' + upload_time + '.txt' # 未來正式上傳的檔名 id會是用戶ID, 副檔名是筆記板檔案的副檔名
        file_path = os.path.join(path, file_name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        context = {
            'status': True,
            'message': '上傳成功!',
            'file_name': file_name,
        }
        return JsonResponse(context)
    
    context = {
            'status': False,
            'error': '上傳過程中出現錯誤'
        }
    return JsonResponse(context)