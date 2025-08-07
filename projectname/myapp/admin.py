from django.contrib import admin
from .models import CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'file')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)