from distutils.command.upload import upload
from django.db import models

# Create your models here.

class ImageData(models.Model):
    
    Imagename = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="img/")