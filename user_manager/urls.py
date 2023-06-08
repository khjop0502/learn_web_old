from django.urls import path
from .views import UserDetail

app_name = "user_manager"
urlpatterns = [
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]