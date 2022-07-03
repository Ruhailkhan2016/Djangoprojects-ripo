from django.urls import path, include
from .import views
urlpatterns = [
    
    path("", views.indexfunc, name = "index"),
    path("home/", views.htmlformfunc, name= "htmlforms"),
   
]