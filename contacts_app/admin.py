from django.contrib import admin
from .models import User_table,Contact_table,Save_search,Limit_table,view_table,Score_tbl,Method_tbl
# Register your models here.
admin.site.register(User_table)
admin.site.register(Contact_table)
admin.site.register(Save_search)
admin.site.register(Limit_table)
admin.site.register(view_table)
admin.site.register(Score_tbl)
admin.site.register(Method_tbl)