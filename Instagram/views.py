from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from annoying.decorators import ajax_request

from Instagram.models import Post, UserLikePost, InstagramUser, UserConnection
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

class UserHomeView(ListView):
    model = Post
    template_name = 'index.html'
    def get_queryset(self):
        current_user = self.request.user
        if(current_user.is_anonymous):
            return None
        following = set()
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)

class UserDetailView(DetailView):
    model = InstagramUser
    template_name = 'user_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'image']
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

@ajax_request
def ToggleFollow(request):
    current_user = InstagramUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstagramUser.objects.get(pk=follow_user_pk)
    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }