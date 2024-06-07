from django.contrib import admin

# Register your models here.
from .models import Employee, Home

admin.site.register(Employee)
admin.site.register(Home)

