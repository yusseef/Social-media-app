from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url='Sign-In')
def upload_post(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user = user, 
        image = image, 
        caption = caption)
        new_post.save()
        return redirect('/')

    else:
        return redirect('/')
    return HttpResponse('upload new post')