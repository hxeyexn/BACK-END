from django.shortcuts import redirect
import requests
from kakao.settings import SOCIAL_OUTH_CONFIG
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# code 요청 함수
# settings.py에 저장한 key 값 불러온 후 redirect 시킴
@api_view(['GET'])
def kakao_login(request):
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRECT_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(CLIENT_ID, REDIRECT_URL)
    res = redirect(url)
    return res

# access token 요청 함수
# 토근의 유저 정보 불러오기
@api_view(['GET'])
def get_user_info(request):
    CODE = request.query_params['code']
    url = "https://kauth.kakao.com/oauth/token"
    res = {
        'grant_type' : 'authorization_code',
        'client_id' : SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
        'redirect_url' : SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
        'client_secret' : SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
        'code' : CODE
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    response = requests.post(url, data=res, headers=headers)
    
    tokenJson = response.json()
    userUrl = "https://kapi.kakao.com/v2/user/me" # api에서 유저 정보 들고오기, nickname, email 보여주기
    auth = "Bearer "+tokenJson['access_token'] # 토큰의 유저 정보를 보기 위해 해당 값만 추출
    HEADER = { # 헤더에 auth 값 넣은 후 토큰의 유저 정보 보기
        "Authorization": auth,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    res = requests.get(userUrl, headers=HEADER)
    return Response(res.text)
