from django import forms
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content', 'image', 'video']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'bio')