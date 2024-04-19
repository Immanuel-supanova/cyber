from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Application

class ApplicationAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        
        # get rsa private key
        # decrypt the token
        
        # Validate token and retrieve app
        token = self.get_validated_token(raw_token)
        
        try:
            app = Application.objects.get(uuid=token['uuid'])
        except Application.DoesNotExist:
            raise AuthenticationFailed('No Developer found')

        return (app, token)
