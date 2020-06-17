from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from Instagram.models import InstagramUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstagramUser
        fields = ('username', 'email', 'profile_picture')