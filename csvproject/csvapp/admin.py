from django.contrib import admin
from csvapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','city','country']

admin.site.register(Employee,EmployeeAdmin)