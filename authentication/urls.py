from django.urls import path
from .views import *

urlpatterns = [
    
    path('profile-settings', profile_settings, name='profile-settings'),
    path('profile/<str:id>', profile, name='profile'),

    path('sign-up', SignUp, name='Sign-Up'),
    path('sign-in', SignIn, name='Sign-In'),
    path('log-out', Logout, name='Log-Out'),



]