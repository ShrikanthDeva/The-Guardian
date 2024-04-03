from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Patient
import re

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

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        # widgets = {
        #     'doctors': forms.Select  # Or any other field you want to render as a dropdown
        # }

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('Phone_Number')
    #     # Check for specific format requirements (e.g., length, numeric characters)
    #     if not re.match(r"^\d{10}$", phone_number):
    #         raise forms.ValidationError("Invalid phone number format. Please enter a 10-digit number.")
    #     return phone_number

    # def clean_email(self):
    #     email = self.cleaned_data.get('Email')
    #     # Use built-in `EmailField` validator by default (checks for valid email syntax)
    #     if not email or not forms.EmailField().clean(email):
    #         raise forms.ValidationError("Please enter a valid email address.")
    #     # Additional checks (e.g., uniqueness in existing user database)
    #     if Patient.objects.filter(email=email).exists():
    #         raise forms.ValidationError("This email address is already registered.")
    #     return email



class DoctorLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')