from django.urls import path, include
from . import views
# from . import views
from users.apps import UsersConfig
from  .views import IndexView, StoryView, AddStoryView, UpdateStoryView, DeleteStoryView, CreateAccountView, AddCommentView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name= 'story'),
    path('add-story/', views.AddStoryView.as_view(), name= 'createStory'),
    path('update-story/<int:pk>/', views.UpdateStoryView.as_view(), name= 'updateStory'),
    path('delete-story/<int:pk>/', views.DeleteStoryView.as_view(), name= 'deleteStory'),
    # path('author/<str:username>', SearchAuthorView.as_view(), name='authorSearch'),
    path('add-comment/<int:pk>/', views.AddCommentView.as_view(), name='addComment'),
    path('users/', include('users.urls')),    
]
