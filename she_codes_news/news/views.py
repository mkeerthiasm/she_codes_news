from django.forms import BaseModelForm
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
# from django.contrib.auth.models import get_user_model
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, StoryCategory
from .forms import StoryForm, CommentForm
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CreateAccountView (generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = "story"

class AddStoryView(generic.CreateView):
        form_class = StoryForm
        context_object_name = 'storyform'
        template_name = 'news/createStory.html'
        success_url = reverse_lazy('news:index')

        def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class UpdateStoryView(generic.UpdateView):
        model = NewsStory
        form_class = StoryForm
        context_object_name = 'storyform'
        template_name = 'news/updateStory.html'
        success_url = reverse_lazy('news:index')

        def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)


class DeleteStoryView(generic.DeleteView):
        model = NewsStory
        context_object_name = 'storyform'
        template_name = 'news/deleteStory.html'
        success_url = reverse_lazy('news:index') 

        def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)       
     
class AddCommentView(generic.CreateView):
        model = NewsStory
        form_class = CommentForm
        context_object_name = 'commentform'
        template_name = 'news/addComment.html'
        success_url = reverse_lazy('news:index')

        def form_valid(self,form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class CategoryView(generic.ListView):
    template_name = 'news'
    context_object_name = 'category'
    model = StoryCategory

    def get_queryset(self):
        return StoryCategory.objects.filter(category=self.kwargs['category'])
               
