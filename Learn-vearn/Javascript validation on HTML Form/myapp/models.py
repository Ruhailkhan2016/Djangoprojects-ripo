from django.db import models

# Create your models here.

class Teacher(models.Model):
    
    Firstname = models.CharField(max_length=50)
    Laststname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    
    
    # this function is used for convererting obejct into string
    def __str__(self) -> str:
        return self.Firstname