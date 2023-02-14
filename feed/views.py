from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost, Followers


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

@login_required(login_url='Sign-In')
def like_post(request, id):
    username = request.user.username
    post_id = id
    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()
    #print(like_filter)
    if like_filter == None:
        
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes -= 1
        post.save()
        return redirect('/')

    #print(username)
    #print(id)
    return HttpResponse('Like post')

@login_required(login_url='Sign-In')
def follow_user(request):
    if request.method == 'POST':
        print(request.POST['follower'])
        print(request.POST['user'])


