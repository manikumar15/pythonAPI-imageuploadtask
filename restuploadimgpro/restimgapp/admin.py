from django.contrib import admin

from .models import Student

class Studentadmin(admin.ModelAdmin):
    list_display = ('sname','image','profile','task')


admin.site.register(Student,Studentadmin)
admin.site.site_header='MANI KUMAR'