from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rôles', {'fields': ('is_student', 'is_teacher', 'is_admin')}),
    )