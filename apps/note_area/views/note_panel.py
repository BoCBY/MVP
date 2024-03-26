import os
from django.shortcuts import render, redirect, HttpResponse

def view_panel(request):
    '''給用戶在線看筆記板檔案內容(暫時先用.txt呈現)'''
    path = request.GET.get('path', '')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            response = HttpResponse(file.read(), content_type='text/plain; charset=utf-8')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
        
        return response
    return HttpResponse("file not found", status=404)