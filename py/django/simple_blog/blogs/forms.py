from django import forms

from .models import BlogPost


class BlogForm(forms.ModelForm):
    """A form for creating a new blog post."""
    class Meta:
        model = BlogPost
        fields = ['title', 'body']
        labels = {'title': '', 'body': ''}



