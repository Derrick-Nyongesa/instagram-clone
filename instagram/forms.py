from django import forms
from .models import Profile, Image, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')