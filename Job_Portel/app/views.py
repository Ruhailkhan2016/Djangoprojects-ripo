from .models import  UserMaster,Candidate,Company,JobDetails,ApplyList
from django.shortcuts import render, redirect
# from random import randint
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

# Index Page View function...///front page
def IndexPage(request):

    return render(request, "app/candidate/index.html")


# Signup page view function..
def SignUp(request):
    
    return render(request, "app/candidate/signup.html")

# User Register Page view function
def RegisterUser(request):
    
    # if request.method == "POST":
    if request.POST['role']=="Candidate":
            
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
    
        user = UserMaster.objects.filter(email=email)
            
            
        if user:
                
            message = "User already exist"

            return render(request, "app/candidate/signup.html", {'msg3' : message})
        else:
                
            if password == cpassword:
                    
                # otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, email=email, password=password)
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                
                messages.success(request, 'Registration successfully completed.')
                # return redirect('loginpage')  
                return redirect('loginpage')  
                
            else:
                    
                # message = "Confirm password does not Match!"
                message = "Confirm password does not Match!"

                return render(request, "app/candidate/signup.html", {'msg1' : message}) 
        
    else:
            
        if request.POST['role']=="Company":
            
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
        
            user = UserMaster.objects.filter(email=email)
            
            if user:
                
                message = "Company already exist"

                return render(request, "app/candidate/signup.html", {'msg3' : message})
    

            else:
                
                if password == cpassword:
                    
                    # otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create(role=role, email=email, password=password)
                    newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                    
                    messages.success(request, 'Registration successfully completed.')
                    return redirect('loginpage')    
                   
                else:
                    
                    # message = "Confirm password does not Match!"
                    message = "Confirm password does not Match!"

                    return render(request, "app/candidate/signup.html", {'msg1' : message})
        else:
            message = "Please select role"
            return render(request, "app/candidate/signup.html", {'msg2' : message})
                
# otppage view function

# def OtpPage(request):
    
#     return render(request, "app/otpverify.html")


# # OTP Verification function
# def OtpVerify(request):

#     email = request.POST['email']
#     otp = int(request.POST['otp'])

#     user = UserMaster.objects.get(email=email)

#     if user:
#         if user.otp == otp:
            
#             message = "OTP Verify successfully"
#             return render(request, "app/login.html", {'msg' : message})
        
#         else:
            
#             message = "OTP is incorrect"
            
#             return render(request, "app/otpverify.html", {'msg' : message, 'email' : email})
    
#     else:
        
#         return render(request, "app/signup.html")
    
        
    
# Login page view function

def Loginpage(request):
    
    return render(request, "app/candidate/login.html")


# create login function for user view
def LoginUser(request):
    try:
        
        if request.POST['role']=="Candidate":
            
            email = request.POST['email']
            password = request.POST['password']
            
            user = authenticate(email=email, password=password)
            # checking the email id with database email id
            user = UserMaster.objects.get(email = email)
            
            
            if user:
                if user.password == password and user.role=="Candidate":
                    
                    can = Candidate.objects.get(user_id=user)

                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = can.firstname
                    request.session['lastname'] = can.lastname
                    request.session['email'] = user.email

                    messages.success(request, 'You were successfully login')
                    
                    return redirect("index")
                
                else:
                    
                    message = "Password does not match!" 
                    return render(request, "app/candidate/login.html", {'msg1' : message})
            
    except:
    
        message="user does not exist"
        return render(request, "app/candidate/login.html", {'msg': message})
        
         
    else:
        
        try:
        
            if request.POST['role']=="Company":
                
                email = request.POST['email']
                password = request.POST['password']
                
                # checking the email id with database email id
                user = UserMaster.objects.get(email = email)
                
                if user:
                    if user.password == password and user.role=="Company":
                        
                        com = Company.objects.get(user_id=user)

                        request.session['id'] = user.id
                        request.session['role'] = user.role
                        request.session['firstname'] = com.firstname
                        request.session['lastname'] = com.lastname
                        request.session['email'] = user.email
                        request.session['password'] = user.password

                        return redirect("companyindex")
                    
                    else:
                        
                        message = "Password does not Match" 
                        return render(request, "app/candidate/login.html", {'msg1' : message})
        except:
            
            message="user does not exist"
            return render(request, "app/candidate/login.html", {'msg': message})

            
        else:
            
            message = "Please select role"
            return render(request, "app/candidate/login.html", {'msg2' : message})




# Logout view function
def Logout(request):
    messages.error(request, 'You were successfully logout')
    try:
        del request.session['email']

    except:
        
        return redirect("index")
    return redirect("loginpage")
    




# User profile page view function 
def ProfilePage(request, pk):
#    i will match it matertable  after matching pk with candidate table
    userMas = UserMaster.objects.get(pk = pk)
    cand    = Candidate.objects.get(user_id = userMas)      # user id is our ForeignKey

    return render(request, "app/candidate/profile.html", {'user' : userMas, 'cand' : cand})
    


# Update profile function
def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk = pk)
    if user.role == "Candidate":
        
        cand = Candidate.objects.get(user_id = user) 
        
        cand.state = request.POST['state']
        cand.city = request.POST['city']
        cand.job_type = request.POST['jobtype']
        cand.jobcategory = request.POST['category']
        cand.highestedu = request.POST['education']
        cand.experience = request.POST['experience']
        cand.website = request.POST['website']
        cand.shift = request.POST['shift']
        cand.min_salary = request.POST['minsalary']
        cand.max_salary = request.POST['maxsalary']
        cand.contact = request.POST['contact']
        cand.gender = request.POST['gender']
        cand.profile_pic = request.FILES['image']
        
        
        messages.success(request, 'Your profile update successfully.')
        
        cand.save()
        url = f'/profilepage/{pk}'    #this is called formating url

        return redirect(url)





# Candidate joblist page
def CandidateJobListPage(request):
    
    all_job = JobDetails.objects.all()
    return render(request, "app/candidate/candidate_job_listing.html", {'all_job' : all_job})
    


# Candidate Job Apply Page Function
def ApplyPage(request, pk):
    
    
    
    user = request.session['id']
    if user:
        
        cand = Candidate.objects.get(user_id = user)
        job = JobDetails.objects.get(id = pk)
        
        return render(request, "app/candidate/apply.html", {'user' : user, 'cand' : cand, 'job' : job})

   

# apply job function
def ApplyJob(request, pk):
    
        user = request.session['id']
        if user:
            
            cand = Candidate.objects.get(user_id = user)
            job = JobDetails.objects.get(pk=pk)
            email = request.POST['email']
            edu = request.POST['education']
            exp = request.POST['experience']
            web = request.POST['website']
            gender = request.POST['gender']
            resume = request.FILES['resume']
            min_salary = request.POST['minsalary']
            max_salary = request.POST['maxsalary']
            
            newapply = ApplyList.objects.create(candidate = cand, job=job, email = email, education = edu, experience=exp, website=web, min_salary=min_salary, max_salary=max_salary, gender=gender, uploadfile=resume)

            
            messages.success(request, "Job Applied Successfully")
            
            return render(request, "app/candidate/apply.html")

    


# about us view function 
def AboutUs(request):
    
    return render(request, 'app/candidate/about.html')



# contact us page views function
def CantactUs(request):
    
    return render(request, 'app/candidate/contact.html')

################################### Company Side ####################################
# company indexpage function
def CompanyIndexPage(request):
    
    return render(request, "app/company/index.html")


# company profile page function
def CompanyProfilePage(request, pk):
    
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    
    return render(request,"app/company/profile.html", {'user' : user, 'comp' : comp})




# update company profile function
def UpdateCompanyProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    
    if user.role == "Company":
        
        
        comp = Company.objects.get(user_id = user)
        
        comp.firstname = request.POST['firstname']
        comp.lastname = request.POST['lastname']
        comp.company_name = request.POST['companyname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.website = request.POST['website']
        # comp.descriptions = request.POST['descriptions']
        comp.logo_pic = request.FILES['image']
        
        comp.save()

        url = f'/companyprofile/{pk}'
        
        return redirect(url)
    
    

# Job Post Page
def JobPostPage(request):
    
    return render(request, "app/company/jobpostpage.html")


# Job Deatl Submit view function
def JobDetailSubmit(request, pk):
    
    user = UserMaster.objects.get(pk = pk)
    if user.role == "Company":
        
        comp = Company.objects.get(user_id = user)
         
        jobname = request.POST['jobname'] 
        companyname = request.POST['companyname'] 
        companyaddress = request.POST['companyaddress'] 
        jobdescription = request.POST['jobdescription'] 
        qualification = request.POST['qualification'] 
        responsibilities = request.POST['responsibilities'] 
        location = request.POST['location'] 
        companywebsite = request.POST['companywebsite'] 
        companyemail = request.POST['companyemail'] 
        companycontact = request.POST['companycontact'] 
        salarypackage = request.POST['salarypackage'] 
        experience = request.POST['experience'] 
        company_logo = request.FILES['logopic']
        
        newjob = JobDetails.objects.create(company_id = comp, jobname = jobname, companyname = companyname, companyaddress = companyaddress, jobdescription = jobdescription, qualification = qualification, responsibilities = responsibilities, location = location, companywebsite = companywebsite, companyemail = companyemail, companycontact = companycontact, salarypackage = salarypackage, experience = experience, company_logo = company_logo)      
        
        message = "Job Post Successfully"

        return render(request, "app/company/jobpostpage.html", {'msg' : message})
    
    



# company logout view functionn
def CompanyLogout(request):
    
   
        del request.session['email']
        del request.session['password']
        

        # message.success(request, "Succesfully Logged Out")
 
        
        return redirect("index")



# Company joblist page
def JobListPage(request):
    
    all_job = JobDetails.objects.all()
    return render(request, "app/company/jobpostlist.html", {'all_job' : all_job})



#Job applied list
def JobAppliedList(request):
    
    all_jobapplied = ApplyList.objects.all()

    return render(request, "app/company/jobappliedlist.html", {'appliedlist' : all_jobapplied})





####################################### Admin Side# ###################################
# admin login page function
def AdminLoginPage(request):
    
    return render(request, "app/admin/login.html")



# admin index page view function
def AdminIndexPage(request):
    
    if 'username' in request.session and 'password' in request.session:
        
        return render(request, "app/admin/adminindex.html")

    else:
        
        return redirect('adminloginpage')


# admin login function
def AdminLogin(request):
    
    username = request.POST['username']
    password = request.POST['password']
    
    if username == "admin" and password == "admin":
        
        request.session['username'] = username
        request.session['password'] = password

        return redirect('adminindex')
    
    else:
        
        message =  "Username and Password does not Match!!"

        return render(request, "app/admin/login.html", {'msg' : message})
    
    

# admin logout view functionn
def AdminLogout(request):
    
   
        del request.session['username']
        del request.session['password']

        # message.success(request, "Succesfully Logged Out")
 
        return redirect("adminloginpage")
    



# admin side User List function 
def AdminUserList(request):
    
    all_user = UserMaster.objects.filter(role="Candidate")

    return render(request, "app/admin/userlist.html", {'alluser' : all_user})




# Company List function 
def AdminCompanyList(request):
    
    all_company = UserMaster.objects.filter(role="Company")

    return render(request, "app/admin/companylist.html", {'allcompany' : all_company})

    


# Delele User function
def UserDelete(request, pk):
    
    user = UserMaster.objects.get(pk=pk)
    user.delete()

    return redirect('userlist')


# Verify company page Function 
def VerifyCompanyPage(request, pk):
    
    company = UserMaster.objects.get(pk=pk)
    
    if company:
        
        return render(request, "app/admin/verify.html", {'company' : company})




# verify Company Function
def VerifyCompany(request, pk):
    
    company = UserMaster.objects.get(pk=pk)

    if company:
        
        company.is_varified = request.POST['verify']
        company.save() 

        return redirect('companylist')
    
    


# Delele Company function
def CompanyDelete(request, pk):
    
    company = UserMaster.objects.get(pk=pk)
    company.delete()

    return redirect('companylist')
