import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse

EXERCISE = os.path.join('structure', 'Server', 'non_cust', 'exercise')
COMPUTER_DESK = os.path.join('C:\\', 'Users', 'admin', 'Desktop')
COMPUTER_EXERCISE_PATH = os.path.join(COMPUTER_DESK, EXERCISE)
NOTEBOOK_DESK = os.path.join('C:\\', 'Users', 'jerry', 'OneDrive', '桌面')
NOTEBOOK_EXERCISE_PATH = os.path.join(NOTEBOOK_DESK, EXERCISE)

def download_pdf(request):
    '''給用戶下載試題檔案'''
    path = request.GET.get('path', '')
    print(path)
    print(type(path))
    if os.path.exists(path):
        with open(path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(path)
        
        if 'one_button' in path:    
            os.remove(path) # 把伺服器裡的一鍵生成檔案刪除, 定期的試題則保留
        return response
    return HttpResponse("PDF file not found", status=404)
    
def serve_pdf(request, subject, date, file_name):
    file_path = os.path.join(COMPUTER_EXERCISE_PATH, subject, 'present', date, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            return response
    return HttpResponse('The requested file was not found.')

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        folder_path = request.GET.get('path', '')
        fs = FileSystemStorage(location=folder_path)
        fs.save(file.name, file)
        return HttpResponse('File uploaded successfully.')
    return HttpResponse('File upload failed.')