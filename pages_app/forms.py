from django import forms
from .models import message, Post
from django.contrib.auth.forms import UserChangeForm
class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    topic = forms.CharField(widget=forms.Textarea(attrs={'rows':5}),required=True)

class PostUpdateForm(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    topic = forms.CharField(widget=forms.Textarea(attrs={'rows':5}),required=True)

