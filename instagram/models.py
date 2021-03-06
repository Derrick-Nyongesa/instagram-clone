from instagram.email import send_welcome_email
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #profile_photo = models.ImageField(upload_to='profile_pics/', default='default.png')
    profile_photo = CloudinaryField('image',null=True, default='default.png')
    bio = models.TextField(max_length=300, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            send_welcome_email(instance.username, instance.email)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @property
    def username(self):
        return self.user.username

class Image(models.Model):
    #image = models.ImageField(upload_to='images/',default='DEFAULT VALUE')
    image = CloudinaryField('image',null=True)
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True, related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    likes = models.IntegerField(default=0)

    class Meta:
       ordering = ['-date_created']

    @property
    def get_all_comments(self):
        return self.comments.all()


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.get(id=image_id)
        return images


    @property
    def get_all_comments(self):
        return self.comments.all()

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return f'{self.user.username if self.user else self.name} Image'


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE,null=True, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.comment} Image'


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'