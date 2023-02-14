from django.contrib import admin
from .models import *
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_display = ['username', 'post_id'] 
admin.site.register(Post)
admin.site.register(LikePost, LikeAdmin)
admin.site.register(Followers)
