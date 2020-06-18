from django.contrib import admin

from Instagram.models import Post, InstagramUser, UserLikePost

# Register your models here.
admin.site.register(Post)
admin.site.register(InstagramUser)
admin.site.register(UserLikePost)