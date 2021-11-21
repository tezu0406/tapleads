from django.shortcuts import render,redirect 
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
    Username=request.POST['Username']
    Password=request.POST['Password']
    User_email=request.POST['User_email']
    User_Phone=request.POST['User_Phone']
    Subscription_type=request.POST['Subscription_type']
    Name=request.POST['Name']
    Status=request.POST['Status']
    User_type=request.POST['User_type']
    
    try:
      user=User_table(Username=Username,Password=Password,User_email=User_email,User_Phone=User_Phone,Subscription_type=Subscription_type,Creation_date=datetime.today(),Name=Name,Status=Status,User_type=User_type)
      user.save()
      message.success(request,'registration succesfully')
      return render(request,'login.html')
      
    expect:
      messages.info(request, 'data already exited')
      

      
      
    
