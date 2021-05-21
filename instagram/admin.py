from instagram.models import Image, Profile, Follow, Comment
from django.contrib import admin

# Register your models here
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Follow)