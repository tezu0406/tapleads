from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from contacts_app.decorators import unauthenticated_user
from contacts_app.models import Contact,UserData,Score
from django.contrib import messages
from django.core import serializers
from contacts_app.models import Contact,UserData,View,SaveSearch,Method,Field
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
import json
from django.db.models import Q
from .tasks import recalculate
import os
import openpyxl

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

@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin','SuperUser'])
def import_record(request):
   user_id=request.session.get('_auth_user_id')
   if user_id == None:
    return redirect('/')
   if request.method=='POST':
        global pd,df,col
        file = request.POST.get('file')  
        file_name,ex=os.path.splitext(file)
        if  ex=='.csv':
         d=pd.read_csv(file)
         
        else:
         d=pd.read_excel(file)
      
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
    return redirect('/dashboard_redirect/view')
  return render(request,'auto_record.html',{'col':col})  

@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','SuperUser'])
def dashboard_free(request):
  user_id=request.session.get('_auth_user_id')
  users=UserData.objects.get(user_id=user_id)
  return render(request,'dashboard_free.html', {'users':users,
                                                'username':request.user.username,
                                                'date_joined':request.user.date_joined
                                                })      
    

@login_required(login_url="login")
@allowed_users(allowed_roles=['paid_subscriber','SuperUser'])
def dashboard_paid(request):
  user_id=request.session.get('_auth_user_id')
  user_data=UserData.objects.get(user_id=user_id)
  return render(request,'dashboard_paid.html', {'user_data':user_data,
                                                'balance': user_data.total_limits - user_data.viewed,
                                                'date_joined':request.user.date_joined})


@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin','SuperUser'])
def dashboard_admin(request):
  user_id=request.session.get('_auth_user_id')
  user_data=UserData.objects.get(user_id=user_id)
  return render(request,'dashboard_admin.html', {'user_data':user_data,
                                                 'username':request.user,
                                                 'balance': user_data.total_limits - user_data.viewed,
                                                 'date_joined':request.user.date_joined,
                                                 })


@login_required(login_url="login")
@allowed_users(allowed_roles=['SuperUser'])
def dashboard_superuser(request):
  user_id=request.session.get('_auth_user_id')
  user_data=UserData.objects.get(user_id=user_id)
  scores=Score.objects.all()
  subscription_type=request.session.get('subscription_type')


  return render(request,'dashboard_superuser.html', {'user_data':user_data,
                                                     'scores':scores,
                                                    'subscription_type':subscription_type,
                                                    'balance': user_data.total_limits - user_data.viewed,
                                                    'date_joined':request.user.date_joined,})



def dashboard_redirect(request):
  user_id=request.session.get('_auth_user_id')
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
@allowed_users(allowed_roles=['free_subscriber','paid_subscriber','Admin','SuperUser'])
def record_show(request):
  s_search=SaveSearch.objects.all()[::-5]
  group = request.user.groups.filter(user=request.user)[0]
  sub_type=str(group.name)
  viewed=View.objects.filter(user=request.user)
  scores=Score.objects.filter(user=request.user)
  contacts = []
  for contact in Contact.objects.all():
        is_viewed = len(viewed.filter(contact_id=contact.id)) != 0
        score = scores.filter(contact=contact).first()
        if score != None:
              score = score.value
        else:
              score = 0
        contacts.append({'is_viewed': is_viewed, 'contact': contact, 'score': score})
  return render(request,'view_records.html',{'contacts': contacts,'sub_type':sub_type,'save':s_search})
  


@login_required(login_url="login")
@allowed_users(allowed_roles=['SuperUser'])
def limit_data(request, id):
  user = request.user
  user_data=UserData.objects.get(user_id=user.id)
  if(user_data.total_limits > user_data.viewed):   
    contact=Contact.objects.get(id=id)
    view = View(user=user, contact=contact)
    view.save()
    user_data.viewed += 1
    user_data.save()
  else:
    return HttpResponse("You have used your allowed limit.")
  return redirect('/dashboard_redirect/view')


@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','paid_subscriber','Admin','SuperUser'])
def save_search(request):
  user_id=request.session.get('_auth_user_id')
  if user_id == None:
    return redirect('/')
  if request.method=='POST':
    u=request.user
    save_search=request.POST.get('save_search')
    save=SaveSearch(user=u,search_criteria=save_search)
    save.save()
    return redirect('/dashboard_redirect/view')
  return redirect('/dashboard_redirect/view')



@login_required(login_url="login")
@allowed_users(allowed_roles=['paid_subscriber','Admin','SuperUser'])
#Export Data
def Export(request):
  ids=[]
  
  data=View.objects.all()
  for i in data:
    ids.append(i.contact_id)
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
        for user in users:
            writer.writerow(user)
        return response
        
 
  return render(request, 'view_records.html')



@login_required(login_url="login")
@allowed_users(allowed_roles=['paid_subscriber','Admin','SuperUser'])
def Export(request):
  ids=[]
  
  data=View.objects.all()
  for i in data:
    ids.append(i.contact_id)
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['SuperUser'])
def set_limits(request):
  if request.method =='POST':
    user_data = UserData.objects.get(user_id = request.POST.get('user_id'))
    user_data.total_limits = request.POST.get('total_limits')
    user_data.save()
  users = User.objects.all()
  users_data = UserData.objects.all()
  custom_users = []
  for user in users:
        custom_users.append({'user': user, 'data': users_data.get(user_id=user.id)})
  return render(request,'set_limits.html', {'custom_users': custom_users})
  
  
@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','paid_subscriber','Admin','SuperUser'])
def set_score(request):
  user_data = UserData.objects.get(user=request.user)
  methods = Method.objects.filter(Q(owner_id=None) | Q(owner_id=request.user.id))
  if request.method == "POST":
        data = json.loads(request.body)
        method = Method(owner=request.user, type='userdefined', name=data['name'])
        method.save()
        for field in data['fields'].values():
          Field(method=method, name=field['field'], weightage=field['weightage']).save()
  return render(request,
                "set_score.html",
                {
                  'current_method': user_data.current_method,
                  'methods': serializers.serialize('json', methods)
                }
  )
  
  
@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','paid_subscriber','Admin','SuperUser'])
def select(request):
      if request.method =='POST':
            method = request.POST.get('method')
            user_data = UserData.objects.get(user=request.user)
            user_data.current_method_id = method
            user_data.save()
            recalculate.apply_async([request.user.id])
      return redirect('/set_score')



@login_required(login_url="login")
@allowed_users(allowed_roles=['free_subscriber','paid_subscriber','Admin','SuperUser'])
def recalculate_score(request):
  recalculate.apply_async([request.user.id])
  return HttpResponse("Done")