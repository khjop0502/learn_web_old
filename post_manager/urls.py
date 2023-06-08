from django.urls import path
from .views import PostList

app_name = "post_manager"
urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
]