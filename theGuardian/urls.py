from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('register/', views.signup),
    path('home/', views.home),
    path('timeline/', views.timeline),
    path('analytics/', views.analytics)
    
    
    #added by ajay kumar
    ,path('about/', views.about),
    path('contact/',views.contact),
    path('patientAdmit/',views.patientAdmit),
    path('patientReAdmit/',views.patientReAdmit)
}