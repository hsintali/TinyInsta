from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from annoying.decorators import ajax_request

from Instagram.models import Post, UserLikePost
from Instagram.forms import CustomUserCreationForm

# Create your views here.
class Home(TemplateView):
    template_name = 'test.html'

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

@ajax_request
def AddLike(request):
    post_pk = request.POST.get('post_pk') 
    post = Post.objects.get(pk=post_pk)
    try:
        like = UserLikePost(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = UserLikePost.objects.get(post=post, user=request.user)
        like.delete()
        result = 0
    return {
        'result': result,
        'post_pk': post_pk
    }