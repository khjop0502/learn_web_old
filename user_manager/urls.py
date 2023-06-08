from django.urls import path
from .views import UserDetail, UserList

app_name = "user_manager"
urlpatterns = [
    path("user/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path('users/', UserList.as_view(), name='user_list'),
]