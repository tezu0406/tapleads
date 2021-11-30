from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from contacts_app import views

urlpatterns = [
    path('', views.login, name='login_reg'),
    path('registration',views.registration, name='registration'),
    path('addrecord',views.Add_record, name='Add_record'),
    path('dashboard_free',views.dashboard_free,name='Dashboard_free'),
]
