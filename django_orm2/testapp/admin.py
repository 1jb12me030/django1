from django.contrib import admin
from testapp.models import Employee
#from django.db.models import Max


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('ename','esal')
admin.site.register(Employee, EmployeeAdmin)    