from django.urls import path
from .views import kakao_login, get_user_info

urlpatterns = [
    path('accounts/kakao/login/', kakao_login),
    path('user/kakao/callback/', get_user_info, name="kakao_callback"),
]