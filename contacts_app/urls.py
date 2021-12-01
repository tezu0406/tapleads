from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from contacts_app import views
from contacts_app import forms
admin.autodiscover()

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login',views.login,name="login"),
    path('registration',views.registration, name='registration'),
    path('addrecord',views.add_record, name='add_record'),
    path('dashboard_free',views.dashboard_free,name='Dashboard_free'),
    path('importrecord',views.import_record,name="import_record"),
]
