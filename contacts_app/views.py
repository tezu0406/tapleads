from django.shortcuts import render,redirect,HttpResponse
from contacts_app.models import Contact
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as loginUser, logout


# Create your views here.
def homepage(request):
  return render(request,"homepage.html")

def login(request):
  user_id=request.session.get('_auth_user_id')
  
  if user_id != None:
    return redirect('/dashboard_free')

  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        loginUser(request, user)
        return redirect("/dashboard_free")
  form = AuthenticationForm()
  return render(request,"login.html",{"form":form})

def logout(request):
  request.session['Username']=None
  return redirect('/')

def registration(request):
  user_id=request.session.get('_auth_user_id')

  if user_id != None:
    return redirect('/')

  if request.method=="POST":
    form = RegistrationForm(request.POST)

    if form.is_valid():
      user = form.save()
      loginUser(request, user)
      return redirect("/dashboard_free")
    else:
      return render(request, 'registration.html', {'form': form})
  
  form = RegistrationForm()
  return render(request,'registration.html',{'form':form})



def add_record(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  if request.method=='POST':
    user = request.user
    contact_type=request.POST.get('contact_type')
    full_name=request.POST.get('full_name')
    first_name=request.POST.get('first_name')
    middle_name=request.POST.get('middle_name')
    last_name=request.POST.get('last_name')
    company=request.POST.get('company')
    designation=request.POST.get('designation')
    emailid=request.POST.get('emailid')
    aadhar=request.POST.get('aadhar')
    pan_card=request.POST.get('pan_card')
    phone=request.POST.get('phone')
    location=request.POST.get('location')
    gender=request.POST.get('gender')
    title=request.POST.get('title')
    department=request.POST.get('department')
    university=request.POST.get('university')
    degree=request.POST.get('degree')
    passing_year=request.POST.get('passing_year') 
    college=request.POST.get('college')
    linkedin=request.POST.get('linkedin')
    facebook=request.POST.get('facebook')
    instagram=request.POST.get('instagram')
    industry=request.POST.get('industry')
    country=request.POST.get('country')
    state=request.POST.get('state')
    pin_code=request.POST.get('pin_code')
    key_skills=request.POST.get('key_skills')
    total_experience=request.POST.get('total_experience')
    years_in_business=request.POST.get('years_in_business')
    cin_no=request.POST.get('cin_no')
    turnover=request.POST.get('turnover')
    date_of_incorporation=request.POST.get('date_of_incorporation')
    employees=request.POST.get('employees')
    ctc=request.POST.get('ctc')
    notes=request.POST.get('notes')
    remarks=request.POST.get('remarks')

    try:
      contact=Contact(
          contact_type=contact_type,
          full_name=full_name,
          first_name=first_name,
          middle_name=middle_name,
          last_name=last_name,
          company=company,
          designation=designation,
          emailid=emailid,
          aadhar=aadhar,
          pan_card=pan_card,
          phone=phone,
          location=location,
          gender=gender,
          title=title,
          department=department,
          university=university,
          degree=degree,
          passing_year=passing_year,
          college=college,
          linkedin=linkedin,
          facebook=facebook,
          instagram=instagram,
          industry=industry,
          country=country,
          state=state,
          pin_code=pin_code,
          key_skills=key_skills,
          total_experience=total_experience,
          years_in_business=years_in_business,
          cin_no=cin_no,
          turnover=turnover,
          date_of_incorporation=date_of_incorporation,
          employees=employees,
          ctc=ctc,
          notes=notes,
          remarks=remarks,
          user_id=user_id)
      contact.save()
      return HttpResponse("Import successful! Click to go back to dashboard")
    except Exception as e:
      print(e)  
      return redirect ('/dashboard_free')
  return render(request,'add_record.html')
    

def import_record(request):
  return render(request,'import_record.html')
      
def import_contacts(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  data=pd.read_csv()
  data.delete_duplicates()
  return render(request,'import_contacts.html')

def dashboard_free(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')

  users=User.objects.all()
  contacts=Contact.objects.all()
  subscription_type=request.session.get('subscription_type')
  return render(request,'dashboard_free.html', {'users':users,'username':request.user.username,'subscription_type':subscription_type})      
    
