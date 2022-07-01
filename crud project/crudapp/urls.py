from django.contrib import admin
from django.urls import path,include
from crudapp import views

urlpatterns = [
    
    path('',views.InsetPageView, name="insertpage"),
    path('insert/',views.InsertData, name="insert"),
    path('showpage/',views.ShowPageView, name="showpage"),
    path('editpage/<int:pk>',views.EditPageView, name="editpage"),
    path('updatepage/<int:pk>',views.UpdateViewPage, name="updatepage"),
    path('deletedata/<int:pk>',views.DeleteDataView, name="deletedata"),

]
