from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_name', 'service_type', 'budget', 'preferred_date', 'created_at')
    search_fields = ('name', 'business_name', 'email', 'phone')
    list_filter = ('service_type', 'preferred_date', 'created_at')
