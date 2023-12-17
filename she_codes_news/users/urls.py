from django.urls import path
from .views import CreateAccountView, account_view, UpdateProfileView
from django.contrib.auth import views as auth_views
app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('my-profile'/, account_view, name='account_view'),
    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
]