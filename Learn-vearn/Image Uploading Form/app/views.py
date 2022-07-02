
from django.shortcuts import render, redirect
from .models import ImageData
# Create your views here.

# Index File View 

def IndexPage(request):
    
    return render(request, "app/index.html")



# Upload Image View 

def UploadImage(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(Imagename=imagename, Image=pics)
        return redirect('show')
    
    
# Image Fetching View

def Imagefetch(request):
    
    all_img = ImageData.objects.all()

    return render(request, 'app/show.html', {'allimg' : all_img})