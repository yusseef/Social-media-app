from django.db import models
import uuid
from datetime import datetime
# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'post_image')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Followers(models.Model):
    follower = models.CharField(max_length = 200)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.user