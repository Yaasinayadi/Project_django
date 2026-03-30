from django.contrib import admin
from .models import Teacher, Department, Subject, Holiday


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_id', 'first_name', 'last_name', 'department']
    search_fields = ['first_name', 'last_name', 'teacher_id']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head_teacher']
    search_fields = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'teacher']
    search_fields = ['name', 'code']


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'start_date', 'end_date']
    search_fields = ['name', 'type']
