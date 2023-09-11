from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from . models import Signup


class SignupAdmin(admin.ModelAdmin):
    list_display=("username","email","phonenumber","address")

admin.site.register(Signup,SignupAdmin)