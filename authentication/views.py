from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='Sign-In')
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

        user_login = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user_login)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credintials')
            return redirect('Sign-In')
    return render(request, 'signin.html')  
@login_required(login_url='Sign-In')
def profile(request):
    user_profile = Profile.objects.get(user = request.user)
    #print(user_profile)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        elif request.FILES.get('image') != None:
            image = request.FILES.get('image') 
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('profile')

    return render(request, 'setting.html', {'user_profile': user_profile})

@login_required(login_url='Sign-In')
def Logout(request):
    auth.logout(request)
    return redirect('Sign-In')