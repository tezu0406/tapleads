from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from contacts_app import views
from contacts_app import forms
admin.autodiscover()

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path('registration',views.registration, name='registration'),
    path('addrecord',views.add_record, name='add_record'),
    path('dashboard_redirect',views.dashboard_redirect,name='dashboard_redirect'),
    path('dashboard_free',views.dashboard_free,name='dashboard_free'),
    path('dashboard_paid',views.dashboard_paid,name='dashboard_paid'),
    path('dashboard_admin',views.dashboard_admin,name='dashboard_admin'),
    path('dashboard_superuser',views.dashboard_superuser,name='dashboard_superuser'),
    path('dashboard_redirect/importrecord',views.import_record,name="file"),
    path('dashboard_redirect/importrecord/import',views.import_contacts,name="import_contacts"),
    path('dashboard_admin/view',views.record_show,name="data"),
    path('dashboard_admin/view/viewed/<id>',views.limit_data,name="data"),
    path('done',views.save_search,name="data"),
    #new
    path('dashboard_paid/view/viewed/<id>',views.limit_data,name="data"),
    path('dashboard_superuser/view/viewed/<id>',views.limit_data,name="data"),
    path('dashboard_admin/Export',views.Export,name="data"),
    path('dashboard_paid/Export',views.Export,name="data"),
    path('dashboard_superuser/Export',views.Export,name="data"),
]
