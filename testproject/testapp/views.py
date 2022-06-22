from django.shortcuts import render
from .forms import Student
# Create your models here.



def showform(request):
    
    fm = Student(request.POST)
    if fm.is_valid():
        
        fname = fm.cleaned_data.get("fname")
        lname = fm.cleaned_data.get("lname")
        email = fm.cleaned_data.get("email")
    
    fm = Student(request.POST)
    
    context = {'forms' : fm, 'fname' : fname, 'lname' : lname, 'email' : email}
    
    
    
    return render(request, 'testapp/home.html', context)