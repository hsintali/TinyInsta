from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from Instagram.models import Post

# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'