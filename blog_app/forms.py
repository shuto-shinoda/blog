from django import forms
from .models import Post, Tag, Comment
from django.forms import ModelForm

class PostAddForm(forms.ModelForm):    
   class Meta:
       model = Post
       fields = ['title', 'text', 'image', 'tag']

class CmtForm(forms.ModelForm):    
   class Meta:
       model = Comment
       fields = ['text']
