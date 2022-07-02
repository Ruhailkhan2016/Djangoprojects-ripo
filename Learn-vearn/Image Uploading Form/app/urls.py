
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings
    
urlpatterns = [
    
    path('', views.IndexPage, name="index"),
    path('upload/', views.UploadImage, name="imageupload"),
    path('showimg/', views.Imagefetch, name="show"),
]

if settings.DEBUG:
    
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)