from django.shortcuts import render
from modelapp.models import User
from .forms import StudentRegistration

# Create your views here.
def addandshow(request):
    if request.method == 'POST':

        # print(request.POST)
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:

        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'putdetail.html', {'form': fm, 'stu' : stud})

