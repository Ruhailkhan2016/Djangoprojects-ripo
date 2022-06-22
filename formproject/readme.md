                    'How to Retrieve Data from a Django Form'

In this project we are creating a form and this form perform simple operation like fill form field and print all the field data in the same page....

step : 1 
settings.py
first of all we have to install our appliaction inside INSTALLED_APPS in settings.py file there already have install some applications in the last we have to write name our application.



step : 2
forms.py
first of all we have create a file form.py and in this form.py file we have import forms module from django module : 'from django import froms', after this we have to create class we can any name of classs so in my we case we take a class name 'student', for create django form we have to create to some fields like first name and last name and email address only this fields we take in our forms. now our form.py file code is complete...

step : 3
views.py
after creating a form fields then we have to create a function for render in html page so we have to go in views.py file in views.py file we create our function, before creating a function you have to import some modules and function.
so first we have to import render in django.shortcut : 'from django.shortcut import render' after you have to import class in from.py file : 'from .form import Student'
after that you have to create a function, we can give any name of our function in my case we have give showform. after create a function you have to write your form class in my case my class name is student for this class we have to create object in my case we give object name is fm and inside bracket() we have pass request.POST it means if user click on submit button then fm object check request it POST or GET if request is POST then it will come in next line in next line it will check our form data is valid or not if our form data is valid then it will come in form fields it will clean every field data after this we have create we create a key for our form object to write this key in html page so we have create a key like : {'forms' : fm} and then if we want to show our form field data in our web page inside the form field so we have to a dictionary for all fields data like : context = {'forms' : fm, 'fname' : fname, 'lname' : lname, 'email' : email} so here in below code you can see we create a dictionary using context object we can show form field output in the above webpage where we have form fields...

after this you can see when we filed our form field data then just click submit button our form field are filled with same data so if we want to clean field after click submit button then we have to give bank form after the form field inside the function like : fm = Student() 

after that we have to return our render function, inside the render function we have pass some parameter like 1.request, 2. html_file_address, 3. dictionary_key.. thats all


step : 4
home.html
aftre creating function in views.py file our next move is create html file here in my case we have give name home.html you can give any name according to project.
inside the html file first of all you have write basic html code if you write '!' exclamation mark and hit enter then necessary code will come automatically....

after this we will come insde the body and there we have write our dictionary key means inside the body we have write our form code like : {{ forms.as_p }} this code we have to inside the form tag, as well as we have to write csrf_token inside the curly braket if we don't include this token form page wil give an error, after this craete a button give name submit...

after that come outside the form tag and there you have to print form fields data so there we give lable tag for each fields here in my case we have first name, last name and email address here we have give 1 field example : '<label for="fname" type>Your First Name : {{fname}}</label><br />' now our html file code is completed


step : 5
urls.py
now come in urls.py and first of all import views module from testapp appliaction,  give the path view function inside the urlpatterns like : 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.showform),
]



  

 