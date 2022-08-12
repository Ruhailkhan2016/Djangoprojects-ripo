
from django.db import models


# Create your models here.

# Master Model
class UserMaster(models.Model):
    
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    # otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_varified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)



# Cadidate model
class Candidate(models.Model):
    
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150) 
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.IntegerField(null = True,blank = True)
    max_salary = models.IntegerField(null = True,blank = True)
    job_type = models.CharField(max_length=150)
    jobcategory = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    highestedu = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    jobdescription = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to = "app/img/candidate")



# Comapany model
class Company(models.Model):
    
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)   
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=250, default="")
    descriptions = models.CharField(max_length=500, default="")
    logo_pic = models.ImageField(upload_to = "app/img/comapany")
    

# job details model
class JobDetails(models.Model):
    
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyemail = models.EmailField(max_length=250)
    companycontact = models.CharField(max_length=50)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.TextField(max_length=500) 
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    salarypackage = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    company_logo = models.ImageField(upload_to="app/img/jobpost", default="")
    



class ApplyList(models.Model):

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    email =models.EmailField(max_length=200)
    education = models.CharField(max_length=200) 
    website = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    
    uploadfile = models.FileField(upload_to="app/resumes/")
    
