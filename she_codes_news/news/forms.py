from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class StoryForm(ModelForm): 
    exclude = ['pub_date']
    class Meta:
        model = NewsStory
        fields = ['title', 'content', 'image_url','category']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Content'}),
            'image_url': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Image URL'}),
            'category': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Category'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','body']
        widgets = {
            'comment': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Comment'}),
            'body': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Body'}),
        }        

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
           
            
            
                                        
                                        