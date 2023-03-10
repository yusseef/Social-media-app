from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from feed.models import Post, Followers
from itertools import chain
# Create your views here.

@login_required(login_url='Sign-In')
def index(request):
    user = Profile.objects.get(user = request.user)

    feed = []
    user_following = Followers.objects.filter(follower = request.user.username)
    user_following_list = [users.user for users in user_following]
    #print(user_following_list)

    for username in user_following_list:
        feed_lists = Post.objects.filter(user = username) | Post.objects.filter(user = request.user.username)
        feed.append(feed_lists)

    
    feed_list = list(chain(*feed))
    print(feed_list)
    posts  = Post.objects.all()

    context = {'user': user, 'posts': feed_list}
    return render(request, 'index.html', context)

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
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()

                user_login = auth.authenticate(username = username, password = password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user = user_model, id_user = user.id)
                new_profile.save()
                return redirect('profile-settings')
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
        print(user_login)
        if user_login is not None:
            auth.login(request, user_login)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credintials')
            return redirect('Sign-In')
    return render(request, 'signin.html')  
@login_required(login_url='Sign-In')
def profile_settings(request):
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
        return redirect('profile-settings')

    return render(request, 'setting.html', {'user_profile': user_profile})

@login_required(login_url='Sign-In')
def Logout(request):
    auth.logout(request)
    return redirect('Sign-In')

def profile(request, id):
    user_object = User.objects.get(username = id)
    user_profile = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user = id)
    posts_length = len(user_posts)
    followers_count = Followers.objects.filter(user = id).count()
    following_count = Followers.objects.filter(follower = id).count()
    print(following_count)

    follower = request.user.username
    user = id

    if Followers.objects.filter(user=user, follower=follower):
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'



    context = {'user_object':user_object, 
    'user_profile': user_profile,
    'user_posts':user_posts,
    'posts_length': posts_length,
    'button_text':button_text,
    'followers_count':followers_count,
    'following_count':following_count}
    return render(request, 'profile.html', context)