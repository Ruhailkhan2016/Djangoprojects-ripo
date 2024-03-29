from django.core import validators
from django import forms
from .models import User 


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        
        model = User
        fields = ['name','address','mobile']
        
        widgets = {
            
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'})
        }