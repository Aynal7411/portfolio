from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Display columns in the admin list view
    search_fields = ('title', 'technologies')  # Enable search by title and technologies
    list_filter = ('created_at',)  # Add a filter sidebar for created_at
