from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class ApplicationTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, app):
        token = super().get_token(app)
        return token

class ApplicationTokenObtainPairView(TokenObtainPairView):
    serializer_class = ApplicationTokenObtainPairSerializer

class AplicationTokenRefreshView(TokenRefreshView):
    serializer_class = ApplicationTokenObtainPairSerializer
