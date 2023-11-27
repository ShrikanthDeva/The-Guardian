from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Patient

class DoctorForm(UserCreationForm):
        
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your Email'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    password2 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    
    phone = forms.CharField(required=True, label="Phone",widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'phone'}))
    specialization = forms.CharField(required=True, label="Specialization",widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Specialization'}))

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'specialization']

class PatientForm(UserCreationForm):

    class Meta:
        model = Patient
        fields = ['patient_name', 'type_of_disease', 'age', 'gender', 'dob', 'doa', 'height', 'weight', 'last_checkup', 'threshold_heart_rate', 'threshold_bp_rate', 'threshold_spo2_rate', 'threshold_co2_rate']

class DoctorLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')