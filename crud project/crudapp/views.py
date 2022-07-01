from webbrowser import get
from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def InsetPageView(request):    
    return render(request, 'app/insert.html')


def InsertData(request):
    # Data come from HTML to view
    
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    
    # Creating Object Of Model Class
    #Inserting data into Table
    newuser = Student.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact)
        
    # After insert render on showpage view
    return redirect('showpage')

# Show Page View
def ShowPageView(request):
    
    # ORM query
    # for featching all the data of the table 
    
    all_data = Student.objects.all() 
    return render(request, 'app/show.html', {'alldata' : all_data})



#Edit Page View
def EditPageView(request, pk):
   
   #featching the data for particular id 
    get_data = Student.objects.get(id = pk)
    return render(request, 'app/edit.html', {'getdata' : get_data})


# Update Data View
def UpdateViewPage(request, pk):
    
    
    udata = Student.objects.get(id = pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    
    #Query for Update
    udata.save()
    #render to show page
    return redirect('showpage')


#Delete Data View
def DeleteDataView(request, pk):
    
    ddata = Student.objects.get(id = pk)

    #Query for Delete
    ddata.delete()

    return redirect('showpage')