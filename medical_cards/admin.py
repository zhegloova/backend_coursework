from django.contrib import admin
from .models import MedicalCard, MedicalRecord

class MedicalRecordInline(admin.TabularInline):
    model = MedicalRecord
    extra = 1
    fields = ('date', 'diagnosis', 'treatment', 'notes')

@admin.register(MedicalCard)
class MedicalCardAdmin(admin.ModelAdmin):
    list_display = ('patient', 'blood_type', 'created_at', 'updated_at')
    list_filter = ('blood_type', 'created_at')
    search_fields = ('patient__last_name', 'patient__first_name', 'allergies', 'chronic_diseases')
    inlines = [MedicalRecordInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('patient', 'blood_type')
        }),
        ('Медицинская информация', {
            'fields': ('allergies', 'chronic_diseases')
        }),
    )

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('medical_card', 'date', 'diagnosis', 'treatment')
    list_filter = ('date', 'medical_card__patient')
    search_fields = ('diagnosis', 'treatment', 'notes', 'medical_card__patient__last_name')
    date_hierarchy = 'date'
    fieldsets = (
        ('Основная информация', {
            'fields': ('medical_card', 'date')
        }),
        ('Медицинская информация', {
            'fields': ('diagnosis', 'treatment', 'notes')
        }),
    )
