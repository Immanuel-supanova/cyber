from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cyber.serializer import AppTokenObtainPairSerializer, AppRefreshTokenSerializer


class ApplicationTokenObtainPairView(TokenObtainPairView):
    serializer_class = AppTokenObtainPairSerializer
    

class AplicationTokenRefreshView(TokenRefreshView):
    serializer_class = AppRefreshTokenSerializer
