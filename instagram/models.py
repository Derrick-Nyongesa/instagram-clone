from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='images/', default='DEFAULT VALUE')
    bio = models.TextField(max_length=300, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return f'{self.user.username} Profile'
