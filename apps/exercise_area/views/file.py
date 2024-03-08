import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse

def download_pdf(request):
    '''給用戶下載一鍵生成的試題檔案'''
    path = request.GET.get('path', '')
    if os.path.exists(path):
        with open(path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(path)
            
        os.remove(path) # 把伺服器裡的一鍵生成檔案刪除
        return response
    else:
        return HttpResponse("PDF file not found", status=404)
    
def view_pdf(request):
    file_path = request.GET.get('path', '')
    if not os.path.exists(file_path) or not file_path.endswith('.pdf'):
        return HttpResponse('Invalid PDF file path.')
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
    return response

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        folder_path = request.GET.get('path', '')
        fs = FileSystemStorage(location=folder_path)
        fs.save(file.name, file)
        return HttpResponse('File uploaded successfully.')
    return HttpResponse('File upload failed.')