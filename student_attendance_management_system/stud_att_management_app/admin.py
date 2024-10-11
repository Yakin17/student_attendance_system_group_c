from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UserModel(UserAdmin): #if I don't create this class password will not be encrypted
    pass

admin.site.register(CustomUser,UserModel)