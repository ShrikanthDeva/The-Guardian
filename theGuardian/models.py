from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=20,null=False, blank=False)
    phone = models.IntegerField(max_length=20, null=False, blank=False)
    specialization = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"

class Patient(models.Model):
    Patient_id = models.AutoField(primary_key=True)
    Patient_Name = models.CharField(max_length=255, null=False, blank=False)
    Reason = models.CharField(max_length=255, null=False, blank=False)
    Age = models.IntegerField(null=False, blank=False)
    Sex = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Non-binary')],null=False, blank=False)
    Blood_Type = models.CharField(max_length=10, blank=True)
    Phone_Number = models.CharField(max_length=20, null=False,blank=False)
    Emergency_Contact_Number = models.CharField(max_length=20, null=False,blank=False)
    Email = models.EmailField(null=False,blank=False,default='')
    DOB = models.DateField(null=False, blank=False)
    DOA = models.DateField(null=False, blank=False)
    Height = models.FloatField(null=True, blank=True)
    Weight = models.FloatField(null=True, blank=True)
    Address = models.CharField(max_length=255, blank=True)
    Insurance_Provider = models.CharField(max_length=50, null=True,blank=True)
    Policy_Number = models.CharField(max_length=20, null=True,blank=True)
    Last_Checkup = models.DateField(null=True, blank=True)
    Pulse = models.IntegerField(null=True, blank=True)
    Blood_Pressure = models.IntegerField(null=True, blank=True)
    Respiration = models.IntegerField(null=True, blank=True)
    Threshold_Heart_Rate = models.IntegerField(null=True, blank=True)
    Threshold_BP_Rate = models.IntegerField(null=True, blank=True)
    Threshold_SPO2_Rate = models.IntegerField(null=True, blank=True)
    Threshold_CO2_Rate = models.IntegerField(null=True, blank=True)
    doctors = models.ManyToManyField(Doctor)


    def __str__(self):
        return f"{self.Patient_Name} ({self.Reason})"

# Create your models here.

class Timeline(models.Model):
    time = models.TimeField()
    description = models.TextField()

# class diseaseinfo(models.Model):

#     patient = models.ForeignKey(Patient , null=True, on_delete=models.SET_NULL)

#     diseasename = models.CharField(max_length = 200)
#     no_of_symp = models.IntegerField()
#     symptomsname = ArrayField(models.CharField(max_length=200))
#     confidence = models.DecimalField(max_digits=5, decimal_places=2)
#     consultdoctor = models.CharField(max_length = 200)