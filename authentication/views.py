from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2:
            if not email or not username or not password:
                messages.error(request, "please fill all fields")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken")
                return redirect('Sign-Up')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('Sign-Up')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'Password dosent match')
            return redirect('Sign-Up')
        
        #print(username)

    return render(request, 'signup.html')