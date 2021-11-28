from django.shortcuts import render,redirect 
from contacts_app.models import User_table,Contact_table,Save_search,Limit_table,view_table,Score_tbl,Method_tbl
from datetime import datetime


# Create your views here.
def login(request):
  Username=request.session.get('Username')
  
  if Username != None:
    return redirect('/')
  
  if request.method=="POST":
    Username=request.POST['Username']
    Password=request.POST['Password']
    User_email=request.POST['User_email'] 
    
    
    try:
      user=User_table.objects.get(Username=Username,Password=Password,User_email=User_email)
    except User_table.DoesNotExist:
      user=None
    
    if user!=None:
      request.session['Username']=Username
      return redirect ('/')
  return render(request,"login.html")

def logout(request):
  request.session['Username']=None
  return redirect('/')

def registration(request):
  Username=request.session.get('Username')
  if Username != None:
    return redirect('/')
  
  if request.method=="POST":
    Name=request.POST['Name']
    User_email=request.POST['User_email']
    Username=request.POST['Username']
    Password=request.POST['Password']
   
    User_Phone=request.POST['User_Phone']
    Subscription_type=request.POST['Subscription_type']
    
    Status=request.POST['Status']
    User_type=request.POST['User_type']
    try:
        user=User_table(Username=Username,Password=Password,User_email=User_email,User_Phone=User_Phone,Subscription_type=Subscription_type,Creation_date=datetime.today(),Name=Name,Status=Status,User_type=User_type)
        user.save()
        
        return render(request,'login.html')
    except:
         return redirect ('/')
  return render(request,'registration.html')

def Add_record(request):
    upload_type=input("manual type press M, file type press F=")
    if upload_type=='M':
      return render(request,'add_record.html')

    elif upload_type=='F':
      return render(request,'import_record.html')
    
    else:
      print("please press correct option!!")
   
      
def import_contacts(request):
  data=pd.read_csv()
  data.delete_duplicates()
  return render(request,'import_contacts.html')
      
    
