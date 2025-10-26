from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create-post'),
]