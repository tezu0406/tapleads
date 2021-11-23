from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from contacts_app import views

urlpatterns = [
    path('',views.login, name='login_reg')
    path('registration',views.registration, name='registration')
]
