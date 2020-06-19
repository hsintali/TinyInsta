import re

from django import template
from django.urls import NoReverseMatch, reverse
from Instagram.models import UserLikePost


register = template.Library()

@register.simple_tag
def is_user_like_post(user, post):
    try:
        like = UserLikePost.objects.get(user=user, post=post)
        return "fa-heart"
    except:
        return "fa-heart-o"

@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_followers().filter(creator=current_user).exists()