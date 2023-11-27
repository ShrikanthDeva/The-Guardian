from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.signup),
    path('home/', views.home, name='home'),
    path('timeline/', views.timeline),
    path('analytics/', views.analytics),
    path('live/', views.live),
]