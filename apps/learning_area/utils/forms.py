import re
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from apps.learning_area import models
from apps.utils.bootstrap import BootstrapModelForm, BootstrapForm
from apps.learning_area.utils import url_conversion, process_time

class FilmModelForm(BootstrapModelForm):
    course = forms.CharField(label='課程名稱', max_length=20, )
    lecturer = forms.CharField(label='授課者', max_length=20, )
    class Meta:
        model = models.FilmInfo
        fields = '__all__'
    
    def clean_course(self):
        txt_course = self.cleaned_data.get('course')
        invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in txt_course:
            if char in invalid_characters:
                raise ValidationError(f'內容不可包含字元:"{char}"')

        return txt_course
    
    def clean_lecturer(self):
        txt_lecturer = self.cleaned_data.get('lecturer')
        invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in txt_lecturer:
            if char in invalid_characters:
                raise ValidationError(f'內容不可包含字元:"{char}"')

        return txt_lecturer
    
    def clean_url(self):
        txt_url = self.cleaned_data.get('url')
        yt_prefix_list = ['https://www.youtube.com/', 'https://youtu.be/', ]
        bili_prefix_list = ['https://www.bilibili.com/', ]
        yt_bili_prefix_list = [item for item in yt_prefix_list] + [item for item in bili_prefix_list]
        from_yt_or_bili = False
        for yt_bili_prefix in yt_bili_prefix_list:
            if txt_url.startswith(yt_bili_prefix):
                from_yt_or_bili = True
                break
        
        if not from_yt_or_bili:
            # 填寫的網址並非yt或b站的影片
            raise ValidationError('目前只接收來自YouTube或bilibili的片源')
                
        for yt_prefix in yt_prefix_list:
            if txt_url.startswith(yt_prefix):
                # yt影片的url處理
                return url_conversion.yt_conversion(txt_url)
        
        if txt_url.startswith(bili_prefix_list[0]):
            # bilibili影片的url處理
            # txt_url = txt_url.replace('')
            return url_conversion.bili_conversion(txt_url)
        
class Description(BootstrapForm):
    start = forms.CharField(label='起始時間', max_length=12)
    end = forms.CharField(label='終止時間', max_length=12)
    description = forms.CharField(label='段落重點', max_length=60)
    
    def clean_start(self):
        txt_start = self.cleaned_data.get('start')
        txt_start = process_time.check_form(txt_start)
        return txt_start
        
    def clean_end(self):
        txt_start = self.cleaned_data.get('start') # 獲取到clean_start的return value, 而不是用戶原始輸入資料
        if not txt_start:
            raise ValidationError("起始時間輸入錯誤")
        txt_end = self.cleaned_data.get('end')
        txt_end = process_time.check_form(txt_end)
        start_time = process_time.total_seconds(txt_start)
        end_time = process_time.total_seconds(txt_end)
        if start_time >= end_time:
            raise ValidationError("終止時間應在起始時間後")
        
        return txt_end
    
    def clean_description(self):
        txt_description = self.cleaned_data.get('description')
        if '-' in txt_description:
            txt_description = txt_description.replace('-', '－') # 在前端頁面中, 倘若在這個輸入框包含'-', 則有些(例如刪除)功能就無法順暢運作.
        invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in txt_description:
            if char in invalid_characters:
                raise ValidationError(f'內容不可包含字元:"{char}"')

        return txt_description