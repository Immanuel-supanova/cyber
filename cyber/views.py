from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cyber.serializer import ApplicationTokenObtainPairSerializer, ApplicationRefreshTokenSerializer


class ApplicationTokenObtainPairView(TokenObtainPairView):
    serializer_class = ApplicationTokenObtainPairSerializer

class AplicationTokenRefreshView(TokenRefreshView):
    serializer_class = ApplicationRefreshTokenSerializer
