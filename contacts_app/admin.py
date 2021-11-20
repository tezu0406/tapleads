from django.contrib import admin
from app.models import User_table,Contact_table,Save_search,Limit_table,view_table
# Register your models here.
admin.site.register(User_table,Contact_table,Save_search,Limit_table,view_table)
