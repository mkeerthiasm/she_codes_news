from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(max_length=500, required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email']                