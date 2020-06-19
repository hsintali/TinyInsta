"""TinyInsta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from Instagram.views import (Home, PostListView, PostDetailView,
                             PostCreateView, PostUpdateView, PostDeleteView,
                             AddLike, UserDetailView, UserHomeView, ToggleFollow)

urlpatterns = [
    path('test/', Home.as_view(), name='test'),
    path('allposts/', PostListView.as_view(), name='allposts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('like/', AddLike, name='addlike'),
    path('togglefollow/', ToggleFollow, name='togglefollow'),
    path('', UserHomeView.as_view(), name='home'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user'),
]
