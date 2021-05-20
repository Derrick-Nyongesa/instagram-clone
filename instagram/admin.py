from instagram.models import Image, Profile, Comment, Follow
from django.contrib import admin

# Register your models here
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Follow)