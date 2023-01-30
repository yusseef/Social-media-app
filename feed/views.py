from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='Sign-In')
def upload_post(request):
    return HttpResponse('upload new post')