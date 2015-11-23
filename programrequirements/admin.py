from django.contrib import admin

from .models import UWUser, Course, ComputerEngineering2015

# Register your models here.
admin.site.register(UWUser)
admin.site.register(Course)
admin.site.register(ComputerEngineering2015)
