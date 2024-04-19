from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from cyber.serializer import AppTokenObtainPairSerializer, AppRefreshTokenSerializer


class ApplicationTokenObtainPairView(TokenObtainPairView):
    serializer_class = AppTokenObtainPairSerializer
    

class AplicationTokenRefreshView(TokenRefreshView):
    serializer_class = AppRefreshTokenSerializer
