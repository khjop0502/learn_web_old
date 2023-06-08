from django.urls import path
import test_viewer.views as tmp

app_name = "test_viewer"
urlpatterns = [
    path('test/', tmp.test_api, name='test_api'),  # 함수 호출 괄호 제거
]