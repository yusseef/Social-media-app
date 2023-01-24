from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from.models import Profile
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
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user = user_model, id_user = user.id)
                new_profile.save()
                return redirect('Sign-Up')
        else:
            messages.info(request, 'Password dosent match')
            return redirect('Sign-Up')
        
        #print(username)

    return render(request, 'signup.html')


def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credintials')
            return redirect('Sign-In')
    return render(request, 'signin.html')  


def Logout(request):
    auth.logout(request)
    return redirect('Sign-In')