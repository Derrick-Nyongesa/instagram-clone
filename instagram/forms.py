from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_photo', 'bio']