from django.contrib import admin
from .models import CV, Project

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'file')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')