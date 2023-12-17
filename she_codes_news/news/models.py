from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):

    CategoryRange = models.TextChoices('CategoryRange', 'World Politics Business Technology Science Sports Entertainment Health')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    image_url = models.CharField(max_length=200)
    category = models.CharField(max_length=200 , choices=CategoryRange.choices, default=CategoryRange.World)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='stories')

    
    def __str__(self):
        return self.title
    
# class StoryCategory(models.Model):
#     category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category

class Comment(models.Model):
    comment = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    story = models.ForeignKey(NewsStory, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.author)