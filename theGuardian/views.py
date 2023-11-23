from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   return render(request, 'index.html')

def signup(request):
   return render(request, 'signup.html')

def home(request):
   return render(request, 'home.html')

def timeline(request):
   return render(request, 'timeline.html')

def analytics(request):
   return render(request, 'analytics.html')
