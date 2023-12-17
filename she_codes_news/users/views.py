from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    
    def form_valid(self,form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response
    
@login_required
def account_view(request):
    user_profile = request.user
    created = UserProfile.objects.get_or_create(user=user_profile)
    user_stories = NewsStory.objects.filter(author=user_profile)
    return render(request, 'users/account.html', {'user': user_profile, 'stories': user_stories})

class UpdateProfileView(UpdateView):
    model=CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/updateProfile.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('news:index')
    




# class SearchAuthorView(generic.ListView):
#     template_name = 'users/authoSearch.html'
#     context_object_name = "all_users"

#     def get_queryset(self):
#         '''Return all news stories.'''
#         return CustomUser.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_users'] = CustomUser.objects.all()[:4]
#         return context