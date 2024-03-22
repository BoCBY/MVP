"""
URL configuration for MVP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from apps.homepage.views import homepage
from apps.learning_area.views import learning
from apps.note_area.views import note, note_panel
from apps.exercise_area.views import exercise, file, like_dislike
from apps.stats_area.views import stats


urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # 配置media資料夾
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    
    
    path('homepage/', homepage.homepage),
    path('learning/', learning.learning),
    path('note/', note.note),
    path('exercise/', exercise.exercise),
    path('stats/', stats.stats),
    path('serve_pdf/', file.serve_pdf),
    path('upload_file/', file.upload_file),
    path('download_answer_panel/', file.download_answer_panel),
    path('like_dislike/', like_dislike.like_dislike),
    path('view_panel/', note_panel.view_panel),
      
]
