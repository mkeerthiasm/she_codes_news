from django.urls import path
from .views import CreateAccountView, account_view, UpdateProfileView
from django.contrib.auth import views as auth_views
from . import views
app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('update-profile/<int:pk>', views.UpdateProfileView.as_view(), name='update_profile'),
    path('account/', account_view, name='account'),
    
]