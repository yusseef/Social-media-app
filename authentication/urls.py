from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('sign-up', SignUp, name='Sign-Up'),

]