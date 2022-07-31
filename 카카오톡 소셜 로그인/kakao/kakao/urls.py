from django.contrib import admin
from django.urls import path
from accounts import views
from django.urls.conf import include
from accounts.views import get_user_info, kakao_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', kakao_login, name='kakao_login'),   # 카카오톡 소셜 로그인 화면
    path('accounts/kakao/login/callback/', get_user_info),  # 유저정보 받아와서 api에 nickname, email 보여주기 
]
