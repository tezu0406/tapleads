from django.contrib import admin

from .models import Contact,SaveSearch,Limit,View,Score,Method
# Register your models here.

admin.site.register(Contact)
admin.site.register(SaveSearch)
admin.site.register(Limit)
admin.site.register(View)
admin.site.register(Score)
admin.site.register(Method)