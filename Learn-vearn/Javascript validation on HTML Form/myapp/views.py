from django.shortcuts import render

# Create your views here.

def indexfunc(request):
    return render(request, 'myapp/index.html') 



def htmlformfunc(request):
    
    return render(request, 'myapp/forms.html')