from django.urls import path, include
from . import views
from  .views import IndexView, StoryView, AddStoryView, UpdateStoryView, DeleteStoryView, CreateAccountView, AddCommentView
from .views import SearchAuthorView, CategoryView, LoginView, LogoutView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('<int:pk>/', views.StoryView.as_view(), name= 'story'),
    path('add-story/', views.AddStoryView.as_view(), name= 'createStory'),
    path('update-story/<int:pk>/', views.UpdateStoryView.as_view(), name= 'updateStory'),
    path('delete-story/<int:pk>/', views.DeleteStoryView.as_view(), name= 'deleteStory'),
    path('author/<str:username>', SearchAuthorView.as_view(), name='authorSearch'),
    path('add-comment/<int:pk>/', views.AddCommentView.as_view(), name='addComment'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls')),    
]
