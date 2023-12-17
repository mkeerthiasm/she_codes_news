from django.contrib import admin
from .models import NewsStory, StoryCategory, Comment

# Register your models here.

admin.site.register(NewsStory)
admin.site.register(StoryCategory)
admin.site.register(Comment)

