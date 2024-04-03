from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('register/', views.signup),
    path('home/', views.home, name='home'),
    path('timeline/', views.timeline),
    
    
    #added by ajay kumar
    path('about/', views.about),
    path('contact/',views.contact),
    path('patientAdmit/',views.patientAdmit),
    path('reAdmitPatient/',views.patientReAdmit),
    path('analytics/', views.analytics),
    path('live/', views.live),
    path('checkdisease/', views.checkdisease),
}