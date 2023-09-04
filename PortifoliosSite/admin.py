from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project


class User_Admin(UserAdmin):
    model = User
    fieldsets = []

class Project_Admin(admin.ModelAdmin):
    model = Project
    list_display = ['name', 'author', 'created_at', 'updated_at']


admin.site.register(User, User_Admin)
admin.site.register(Project, Project_Admin)