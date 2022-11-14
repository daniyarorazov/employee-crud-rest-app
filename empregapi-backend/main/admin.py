from django.contrib import admin

from main.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'contact', 'address']
admin.site.register(Employee, EmployeeAdmin)