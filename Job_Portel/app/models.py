
# This code is a Python module that defines the models for a Django web application. 
# The module defines four classes, UserMaster, Candidate, Company, JobDetails and ApplyList, each representing a database table.

from django.db import models


# Create your models here.

# Master Model

# UserMaster is a master model that contains fields for a user's email, password, role, and status. 
# This model can be used for authentication and authorization purposes.
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

# Candidate represents a candidate who is looking for a job. 
# It contains fields for the candidate's personal information, job preferences, and education.
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

# Company represents a company that is hiring. 
# It contains fields for the company's information, such as name, contact information, and description.
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

# JobDetails contains information about a specific job opening, such as the job name, qualifications, responsibilities, location, and salary.
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
    


# Apply List model

# ApplyList is a model that is used to store information about candidates who have applied for a job. 
# It contains fields for the candidate's information, the job they applied for, and their resume.
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
    
    
    
    

# Each model is a subclass of Django's models.Model class and defines its fields using subclasses of models.Field. 
# These fields specify the types and constraints of the data that will be stored in the database.

# For example, models.CharField is used to define a field for storing a string, and models.IntegerField is used to define a field for storing an integer. 
# The ForeignKey field is used to establish a one-to-many relationship between two models.

# The FileField and ImageField fields are used to store files and images, respectively.

# In addition to the fields, each model also specifies a set of methods and properties that define how the model interacts with the database and 
# how it is displayed in the Django admin interface.
    
