from django.urls import path
from .views import *
urlpatterns = [
    path('upload/', upload_post, name = 'upload_post'),
    path('like/<str:id>', like_post, name = 'like_post'),

]