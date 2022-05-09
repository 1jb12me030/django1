from django.contrib import admin
from testapp.models import Employee

# Register your models here.
@admin.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    list_display=('name','sal','addr','age')
    