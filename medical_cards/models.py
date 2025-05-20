from django.db import models
from patients.models import Patient

class MedicalCard(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_card',
        verbose_name='Пациент'
    )
    blood_type = models.CharField(
        max_length=3,
        choices=BLOOD_TYPE_CHOICES,
        blank=True,
        verbose_name='Группа крови'
    )
    allergies = models.TextField(blank=True, verbose_name='Аллергии')
    chronic_diseases = models.TextField(blank=True, verbose_name='Хронические заболевания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Медицинская карта'
        verbose_name_plural = 'Медицинские карты'
        ordering = ['-created_at']

    def __str__(self):
        return f"Медицинская карта {self.patient}"

class MedicalRecord(models.Model):
    medical_card = models.ForeignKey(
        MedicalCard,
        on_delete=models.CASCADE,
        related_name='records',
        verbose_name='Медицинская карта'
    )
    diagnosis = models.TextField(verbose_name='Диагноз')
    treatment = models.TextField(verbose_name='Лечение')
    notes = models.TextField(blank=True, verbose_name='Примечания')
    date = models.DateField(verbose_name='Дата посещения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Запись в медицинской карте'
        verbose_name_plural = 'Записи в медицинской карте'
        ordering = ['-date']

    def __str__(self):
        return f"Запись от {self.date} - {self.diagnosis[:50]}"
