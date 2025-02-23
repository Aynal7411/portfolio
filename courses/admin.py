from django.contrib import admin
from .models import Course, Enrollment

# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'price', 'created_at')  # Fields to display in list view
    search_fields = ('title', 'description')  # Search fields
    list_filter = ('created_at',)  # Filter options
    ordering = ('-created_at',)  # Order by creation date (latest first)

admin.site.register(Course, CourseAdmin)

# Enrollment Admin
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'created_at')  # Fields to display in list view
    search_fields = ('name', 'email', 'course__title')  # Search fields (you can search by course title)
    list_filter = ('created_at', 'course')  # Filter options
    ordering = ('-created_at',)  # Order by creation date (latest first)

admin.site.register(Enrollment, EnrollmentAdmin)
