from django.shortcuts import render,redirect,HttpResponse
from contacts_app.decorators import unauthenticated_user
from contacts_app.models import Contact,UserData
from django.contrib import messages
from contacts_app.models import Contact,UserData,View,SaveSearch
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user
from .forms import RegistrationForm
from django.db import transaction
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
import pandas as pd
import numpy as np
import time
import csv

# Create your views here.
def homepage(request):
  return render(request,"homepage.html")

@unauthenticated_user
def login(request):
    if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
          loginUser(request, user)
          return redirect("/dashboard_redirect")
    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})

def logout(request):
  logoutUser(request)
  return redirect('/')

@unauthenticated_user
def registration(request):
    if request.method=="POST":
      form = RegistrationForm(request.POST)

      if form.is_valid():
        user = form.save()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        subscription_type=request.POST.get('subscription_type')
        user_data = UserData(user=user, name=name, phone_number=phone_number, subscription_type=subscription_type, email=email)
        user_data.save()
        messages.success(request,"Registration successful!")
        return redirect("/login")
      else:
        return render(request, 'registration.html', {'form': form})
    
    form = RegistrationForm()
    return render(request,'registration.html',{'form':form})


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin','SuperUser'])
def add_record(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  if request.method=='POST':
    user = request.user
    status="view"
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
          status=status,
          user_id=user_id)
      contact.save()
      return HttpResponse("Import successful! Click to go back to dashboard")
    except Exception as e:
      print(e)  
      return redirect ('/dashboard_redirect')
  return render(request,'add_record.html')
    


#ADD NEW 
df=''
col=""
def import_record(request):
   user_id=request.session.get('_auth_user_id')
   if user_id == None:
    return redirect('/')
   if request.method=='POST':
        global pd,df,col
        file = request.POST.get('file')        
        d=pd.read_csv(file)
        df=pd.DataFrame(d)
        df.insert(0, "choose options", None)
        col=list(df.columns)
        for i in range(0,len(col)):
          df=df.rename(columns={col[i]:"_".join(col[i].split())})
        col=list(df.columns)
        return redirect('/dashboard_redirect/importrecord/import')
   return render(request,'importrecord.html')


@allowed_users(allowed_roles=['Admin','SuperUser'])
@transaction.atomic  
def import_contacts(request):
  global pd,df,col
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  if request.method=='POST':
    status="view"
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
    for r in df.itertuples():
          print(getattr(r,full_name))
          contact=Contact(
          full_name=getattr(r,full_name),
          first_name=getattr(r,first_name),
          middle_name=getattr(r,middle_name),
          last_name=getattr(r,last_name),
          company=getattr(r,company),
          designation=getattr(r,designation),
          emailid=getattr(r,emailid),
          aadhar=getattr(r,aadhar),
          pan_card=getattr(r,pan_card),
          phone=getattr(r,phone),
          location=getattr(r,location),
          gender=getattr(r,gender),
          title=getattr(r,title),
          department=getattr(r,department),
          university=getattr(r,university),
          degree=getattr(r,degree),
          passing_year=getattr(r,passing_year),
          college=getattr(r,college),
          linkedin=getattr(r,linkedin),
          facebook=getattr(r,facebook),
          instagram=getattr(r,instagram),
          industry=getattr(r,industry),
          country=getattr(r,country),
          state=getattr(r,state),
          pin_code=getattr(r,pin_code),
          key_skills=getattr(r,key_skills),
          total_experience=getattr(r,total_experience),
          years_in_business=getattr(r,years_in_business),
          cin_no=getattr(r,cin_no),
          turnover=getattr(r,turnover),
          date_of_incorporation=getattr(r,date_of_incorporation),
          employees=getattr(r,employees),
          ctc=getattr(r,ctc),
          notes=getattr(r,notes),
          remarks=getattr(r,remarks),
          status=status,
          user_id=user_id)
          print(contact.__dict__)
          contact.save()
          time.sleep(0)
    return redirect('/view')
  return render(request,'auto_record.html',{'col':col})  

@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','SuperUser'])
def dashboard_free(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')

  users=UserData.objects.get(user_id=user_id)
  contacts=Contact.objects.all()
  subscription_type=request.session.get('subscription_type')

  return render(request,'dashboard_free.html', {'users':users,
                                                'username':request.user.username,
                                                'subscription_type':subscription_type,
                                                'date_joined':request.user.date_joined
                                                })      
    

@login_required(login_url="login")
@allowed_users(allowed_roles=['paid_subscriber','SuperUser'])
def dashboard_paid(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')

  users=UserData.objects.get(user_id=user_id)
  contacts=Contact.objects.all()
  balance=request.session.get('balance')
  total_limits=request.session.get('total_limits')
  subscription_type=request.session.get('subscription_type')
  full_name=request.session.get('full_name')
  company=request.session.get('company')

  return render(request,'dashboard_paid.html', {'users':users,
                                                'subscription_type':subscription_type,
                                                'date_joined':request.user.date_joined,
                                                'balance':balance,
                                                'total_limits':total_limits,
                                                'full_name':full_name,
                                                'company':company,
                                                })


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin','SuperUser'])
def dashboard_admin(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')

  users=UserData.objects.get(user_id=user_id)
  print(users)
  contacts=Contact.objects.all()
  username=request.session.get('username')
  balance=request.session.get('balance')
  total_limits=request.session.get('total_limits')

  full_name=request.session.get('full_name')
  company=request.session.get('company')

  return render(request,'dashboard_admin.html', {'users':users,
                                                 'username':request.user,
                                                 'date_joined':request.user.date_joined,
                                                 'balance':balance,
                                                 'total_limits':total_limits,
                                                 'full_name':full_name,
                                                 'company':company,
                                                 })


@login_required(login_url="login")
@allowed_users(allowed_roles=['SuperUser'])
def dashboard_superuser(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')

  users=UserData.objects.get(user_id=user_id)
  contacts=Contact.objects.all()
  subscription_type=request.session.get('subscription_type')


  return render(request,'dashboard_superuser.html', {'users':users,
                                                 'subscription_type':subscription_type,
                                                 'date_joined':request.user.date_joined,})



def dashboard_redirect(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
        return redirect('/')
      
  group = request.user.groups.filter(user=request.user)[0]
  if group.name=="free_subscriber":
      return redirect('/dashboard_free')
  elif group.name=="paid_subscriber":
      return redirect('/dashboard_paid')
  elif group.name=="Admin":
      return redirect('/dashboard_admin')
  elif group.name=="SuperUser":
        return redirect('/dashboard_superuser')  
  
  
# new
#view records
#sub_type=input("Enter a type=")

@login_required(login_url="login")
def record_show(request):
  user_id=request.session.get('_auth_user_id')
  s_search=SaveSearch.objects.all()[::-5]
  group = request.user.groups.filter(user=request.user)[0] 
  sub_type=str(group.name)
  print(sub_type)
  contacts=Contact.objects.all()
  return render(request,'view_records.html',{'contacts':contacts,'sub_type':sub_type,'save':s_search})
  
total_limit=100
def limit_data(request,id):
  user_id=request.session.get('_auth_user_id')
  global total_limit,View
  view=1
  
  total_limit=int(total_limit)-int(view)
  u=request.user
  view=View(user=u,view_contact=int(id))
  contact=Contact.objects.get(id=id)
  contact.status="Viewed"
  contact.save()
  view.save()
  return redirect('/dashboard_admin/view')


@login_required(login_url="login")
def save_search(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  if request.method=='POST':
    u=request.user
    save_search=request.POST.get('save_search')
    save=SaveSearch(user=u,search_criteria=save_search)
    save.save()
    return redirect('/dashboard_admin/view')
  return redirect('/dashboard_admin/view')

#Export Data
def Export(request):
  ids=[]
  
  data=View.objects.all()
  for i in data:
    ids.append(i.view_contact)
  new_id=set(ids)
  if request.method != 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="TapLeads.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Contacts Details'])       
                 
        
        writer.writerow(['full_name','first_name','middle_name','last_name','company','designation','emailid','aadhar','pan_card'	,'phone','location',	'gender','title',	'department','university','degree','	passing_year','college','linkedin','facebook','instagram','industry','country','pin_code','key_skills','total_experience','years_in_business','cin_no',	'turnover','date_of_incorporation','employees','ctc','notes','remarks'])
        
        users=[]
        for i in new_id:
            users.extend(Contact.objects.filter(id=int(i)).values_list('full_name','first_name',	'middle_name',	'last_name','company','designation','emailid','aadhar','pan_card'	,'phone','location',	'gender','title',	'department','university','degree','passing_year','college','linkedin','facebook','instagram','industry','country','pin_code','key_skills','total_experience','years_in_business','cin_no',	'turnover','date_of_incorporation','employees','ctc','notes','remarks'))
        print(users)
        for user in users:
            writer.writerow(user)
        return response
        
 
  return render(request, 'view_records.html')







@login_required(login_url="login")
@allowed_users(allowed_roles=['SuperUser'])
def set_limits(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  group = request.user.groups.filter(user=request.user)[0]
  total_limits=request.session.get('total_limits')
  balance=request.session.get('balance')
  users=UserData.objects.get(user_id=user_id)
  sub_type=str(group.name)
  return render(request,'set_limits.html', {'users':users,
                                            'total_limits':total_limits,
                                            'sub_type':sub_type,
                                            'balance':balance
                                            })

  


def Export(request):
  ids=[]
  
  data=View.objects.all()
  for i in data:
    ids.append(i.view_contact)
  new_id=set(ids)
  if request.method != 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="TapLeads.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Employee Detail'])       
                 
         
        writer.writerow(['full_name','first_name','middle_name','last_name','company','designation','emailid','aadhar','pan_card'	,'phone','location',	'gender','title',	'department','university','degree','	passing_year','college','linkedin','facebook','instagram','industry','country','pin_code','key_skills','total_experience','years_in_business','cin_no',	'turnover','date_of_incorporation','employees','ctc','notes','remarks'])
        
        users=[]
        for i in new_id:
            users.extend(Contact.objects.filter(id=int(i)).values_list('full_name','first_name',	'middle_name',	'last_name','company','designation','emailid','aadhar','pan_card'	,'phone','location',	'gender','title',	'department','university','degree','passing_year','college','linkedin','facebook','instagram','industry','country','pin_code','key_skills','total_experience','years_in_business','cin_no',	'turnover','date_of_incorporation','employees','ctc','notes','remarks'))
        
        for user in users:
            writer.writerow(user)
        return response
        
 
  return render(request, 'view_records.html')
