from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

# Create your models here.
class InstagramUser(AbstractUser):
    profile_picture = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'jpeg',
        options = {'quality': 100},
        blank = True,
        null = True,
    )

class Post(models.Model):
    author = models.ForeignKey(
        InstagramUser,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
        related_name = 'posts',
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'jpeg',
        options = {'quality': 100},
        blank = True,
        null = True,
    )
    posted_on = models.DateTimeField(
        auto_now_add = True,
        editable = False,
    )

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
    
    def get_like_count(self):
        return self.likes.count()

class UserLikePost(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'likes',
    )
    user = models.ForeignKey(
        InstagramUser,
        on_delete = models.CASCADE,
        related_name = 'likes',
    )

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title