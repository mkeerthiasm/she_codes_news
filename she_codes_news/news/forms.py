from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm): 
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateInput(format = '%m, %d, %Y',attrs = {'type': 'date', 'class': 'form-control', 'placeholder': 'Select a date', 'id': 'pub_date'})},
        
                                        
                                        