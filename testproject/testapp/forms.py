from django import forms


class Student(forms.Form):
    
    fname = forms.CharField(label="First Name", max_length=70)
    lname = forms.CharField(label="Last Name", max_length=70)
    email = forms.EmailField(label="Email Address", max_length=70)