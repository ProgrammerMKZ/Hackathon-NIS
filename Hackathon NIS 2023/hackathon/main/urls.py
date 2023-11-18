from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.sus),
    path('login', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('show/', views.file_show, name='file_show')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)