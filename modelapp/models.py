from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    mobile = models.IntegerField()