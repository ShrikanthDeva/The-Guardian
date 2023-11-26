from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=20,null=False, blank=False)
    phone = models.IntegerField(max_length=20, null=False, blank=False)
    specialization = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return f"Dr. {self.doctor.username} ({self.specialization})"

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255, null=False, blank=False)
    type_of_disease = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=20, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    doa = models.DateField(null=False, blank=False)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    last_checkup = models.DateField(null=True, blank=True)
    threshold_heart_rate = models.IntegerField(null=True, blank=True)
    threshold_bp_rate = models.IntegerField(null=True, blank=True)
    threshold_spo2_rate = models.IntegerField(null=True, blank=True)
    threshold_co2_rate = models.IntegerField(null=True, blank=True)
    doctors = models.ManyToManyField(Doctor)


    def __str__(self):
        return f"{self.patient_name} ({self.type_of_disease})"

# Create your models here.

class Timeline(models.Model):
    time = models.TimeField()
    description = models.TextField()