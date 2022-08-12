from django.urls import path
from app import views


urlpatterns = [

    ############################# Candidate Side ##################################
    
    path("", views.IndexPage, name="index"),
    path("signup/", views.SignUp, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    
    # path("otppage/", views.OtpPage, name="otppage"),
    # path("otp/", views.OtpVerify, name="otp"),
    
    path("loginpage/", views.Loginpage, name="loginpage"),
    path("loginuser/", views.LoginUser, name="login"),
    path("logout/", views.Logout, name="logout"),
    
    path("profilepage/<int:pk>", views.ProfilePage, name="profilepage"),
    path("updateprofile/<int:pk>", views.UpdateProfile, name="updateprofile"),
    
    path("candjoblistpage", views.CandidateJobListPage, name="candjoblistpage"),
    
    path("apply/<int:pk>", views.ApplyPage, name="apply"),
    path("applyjob/<int:pk>", views.ApplyJob, name="applyjob"),
    
    
    path("aboutuspage", views.AboutUs, name="aboutus"),
    path("contactuspage", views.CantactUs, name="contactus"),
    
    
    
    ############################# Company Side ##################################
    
    path("companyindex/", views.CompanyIndexPage, name="companyindex"),
    path("companyprofile/<int:pk>", views.CompanyProfilePage, name="companyprofile"),
    path("updatecompanyprofile/<int:pk>", views.UpdateCompanyProfile, name="updatecompanyprofile"),
    
    
    path("jobpostpage/", views.JobPostPage, name="jobpostpage"),
    path("jobpost/<int:pk>", views.JobDetailSubmit, name="jobpost"),
    
    
    path("companylogout", views.CompanyLogout, name="companylogout"),
    path("jobpostlist", views.JobListPage, name="jobpostlist"),
    path("candidateappliedlist", views.JobAppliedList, name="candidateappliedlist"),
    
    
    
    
    ####################################### Admin Side# ###################################
    
    path("adminloginpage/", views.AdminLoginPage, name="adminloginpage"),
    path("adminindex/", views.AdminIndexPage, name="adminindex"),
    
    path("adminlogin/", views.AdminLogin, name="adminlogin"),
    path("adminlogut/", views.AdminLogout, name="adminlogut"),
    
    path("adminuserlist/", views.AdminUserList, name="userlist"),
    path("admincompanylist/", views.AdminCompanyList, name="companylist"),
    
    path("deleteuser/<int:pk>", views.UserDelete, name="userdelete"),
    path("deletecompany/<int:pk>", views.CompanyDelete, name="companydelete"),
    
    path("verifycompanypage/<int:pk>", views.VerifyCompanyPage, name="verifypage"),
    path("verifycompany/<int:pk>", views.VerifyCompany, name="verify"),
    
    
    
    
    
    
    
    
]
 
