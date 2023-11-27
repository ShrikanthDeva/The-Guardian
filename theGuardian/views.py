from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorForm, DoctorLoginForm, PatientForm
from .models import Doctor, Patient
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Timeline

# Create your views here.

def index(request):
   # if request.user.is_authenticated:
   #    return HttpResponse(reverse('home'))
   
   if request.method == 'POST':
      form = DoctorLoginForm(data = request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']

         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse('home'))
      else:
         return render(request, 'index.html', context={'form': form, 'error': 'Invalid username or password'})
         
   else:
      form = DoctorLoginForm()
      return render(request, 'index.html', context={'form': form, 'error': ''})

def signup(request):
   # if request.user.is_authenticated:
   #    return HttpResponse(reverse('home'))
   error = ''
   form = DoctorForm()
   if request.method == 'POST':
      form = DoctorForm(request.POST)
      print(form['username'],form['email'],form['password1'],form['password2'],form['phone'],form['specialization'])
      if form.is_valid():

         print(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password1'],form.cleaned_data['password2'],form.cleaned_data['phone'],form.cleaned_data['specialization'])
         user = form.save()
         doctor_profile = Doctor(user = user, phone = form.cleaned_data['phone'], specialization = form.cleaned_data['specialization'])
         doctor_profile.save()
         user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
         if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse('home'))
         else:
            return HttpResponseRedirect(reverse('index.html'))
      else:
         if User.objects.filter(username=request.POST['username']).exists():
            error = 'Doctor already exists'

         else:
            error = 'Your password is not strong enough or both password must be same'
   
   return render(request, 'signup.html',context={'form': form,'error': error})

def home(request):
   return render(request, 'home.html')

def timeline(request):
   return render(request, 'timeline.html')

def analytics(request):
   return render(request, 'analytics.html')

def live(request):
   return render(request, 'graphs2.html')