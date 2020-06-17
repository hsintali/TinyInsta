from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'jpeg',
        options = {'quality': 100},
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class InstagramUser(AbstractUser):
    profile_picture = ProcessedImageField(
        upload_to = 'static/images/profile',
        format = 'jpeg',
        options = {'quality': 100},
        blank=True,
        null=True,
    )