from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'gender', 'phone_number')
    list_filter = ('gender', 'date_of_birth')
    search_fields = ('last_name', 'first_name', 'middle_name', 'phone_number', 'email')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        ('Основная информация', {
            'fields': ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'gender')
        }),
        ('Контактная информация', {
            'fields': ('phone_number', 'email', 'address')
        }),
    )
