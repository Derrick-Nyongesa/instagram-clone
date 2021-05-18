from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='profile_pics/', default='DEFAULT VALUE')
    bio = models.TextField(max_length=300, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return f'{self.user.username} Profile'


class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='DEFAULT VALUE')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', related_name='images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Image'


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default='', related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'