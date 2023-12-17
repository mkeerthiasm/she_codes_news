from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# Create your views here.
    
class LoginView(generic.TemplateView):
    template_name = 'users/login.html'

class LogoutView(generic.TemplateView):
    template_name = 'users/logout.html'





class SearchAuthorView(generic.ListView):
    template_name = 'users/authoSearch.html'
    context_object_name = "all_users"

    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_users'] = CustomUser.objects.all()[:4]
        return context