from django.shortcuts import render,redirect 
from contacts_app.models import User_table,Contact_table,Save_search,Limit_table,view_table,Score_tbl,Method_tbl
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
def login(request):
  Username=request.session.get('Username')
  
  if Username != None:
    return redirect('/dashboard_free')
  
  if request.method=="POST":
    Username=request.POST['Username']
    Password=request.POST['Password']
    
    
    try:
      user=User_table.objects.get(Username=Username,Password=Password)

    except User_table.DoesNotExist:
      user=None
    
    if user != None:
      request.session['Username'] = Username
      return redirect ('/dashboard_free')
  return render(request, "login.html")

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
    try:
        user=User_table(
          Username=Username,
          Password=Password,
          User_email=User_email,
          User_Phone=User_Phone,
          Subscription_type=Subscription_type,
          Creation_date=datetime.today(),
          Name=Name,
          Status="N",
          User_type="Subscriber")
        user=User.objects.create_user(Username, Password, User_email)
        user.save()
        
        return render(request,'dashboard_free.html')
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

  Username=request.session.get('Username')
  if Username== None:
    return redirect('/')

  if request.method=='POST':
    Contact_ID=request.POST['Contact_ID']
    Contact_type=request.POST['Contact_type']
    Full_name=request.POST['Full_name']
    First_name=request.POST['First_name']
    Middle_name=request.POST['Middle_name']
    Last_name=request.POST['Last_name']
    Company=request.POST['Company']
    Designation=request.POST['Designation']
    Emailid=request.POST['Emailid']
    Aadhar=request.POST['Aadhar']
    Pan_card=request.POST['Pan_card']
    Phone=request.POST['Phone']
    Location=request.POST['Location']
    Gender=request.POST['Gender']
    Title=request.POST['Title']
    Department=request.POST['Department']
    University=request.POST['University']
    Degree=request.POST['Degree']
    Passing_year=request.POST['Passing_year']
    College=request.POST['College']
    LinkedIN=request.POST['LinkedIN']
    Facebook=request.POST['Facebook']
    Instagram=request.POST['Instagram']
    Industry=request.POST['Industry']
    Country=request.POST['Country']
    State=request.POST['State']
    Zip=request.POST['Zip']
    Key_Skills=request.POST['Key_Skills']
    Total_Experience=request.POST['Total_Experience']
    Years_in_Business=request.POST['Years_in_Business']
    CIN_No=request.POST['CIN_No']
    Turnover=request.POST['Turnover']
    Date_of_Incorporation=request.POST['Date_of_Incorporation']
    Employees=request.POST['Employees']
    CTC=request.POST['CTC']
    Notes=request.POST['Notes']
    Remarks=request.POST['Remarks']
    user_id=request.POST['user_id']

    try:
      contact=Contact_table(
        Contact_ID=Contact_ID,
        Contact_type=Contact_type,
        Full_name=Full_name,
        First_name=First_name,
        Middle_name=Middle_name,
        Last_name=Last_name,
        Company=Company,
        Designation=Designation,
        Emailid=Emailid,
        Aadhar=Aadhar,
        Pan_card=Pan_card,
        Phone=Phone,
        Location=Location,
        Gender=Gender,
        Title=Title,
        Department=Department,
        University=University,
        Degree=Degree,
        Passing_year=Passing_year,
        College=College,
        LinkedIN=LinkedIN,
        Facebook=Facebook,
        Instagram=Instagram,
        Industry=Industry,
        Country=Country,
        State=State,
        Zip=Zip,
        Key_Skills=Key_Skills,
        Total_Experience=Total_Experience,
        Years_in_Business=Years_in_Business,
        CIN_No=CIN_No,
        Turnover=Turnover,
        Date_of_Incorporation=Date_of_Incorporation,
        Employees=Employees,
        CTC=CTC,
        Notes=Notes,
        Remarks=Remarks,
        user_id=user_id)
      contact.save()
      return render(request,'dashboard_free.html')
    except:
         return redirect ('/')
  return render(request,'dashboard_free.html')

  
      
def import_contacts(request):
  Username=request.session.get('Username')
  if Username == None:
    return redirect('/')
  data=pd.read_csv()
  data.delete_duplicates()
  return render(request,'import_contacts.html')

def dashboard_free(request):
  Username=request.session.get('Username')
  if Username == None:
    return redirect('/')
  users=User_table.objects.all()
  contacts=Contact_table.objects.all()
  Subscription_type=request.session.get('Subscription_type')
  return render(request,'dashboard_free.html', {'users':users,'Username':Username,'Subscription_type':Subscription_type})      
    
