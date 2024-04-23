import ast
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding 

from .models import Application
from cyber.key import decrypt_data, private_key, remove_padding

class ApplicationAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None
        data = request.data
        key_bytes = ast.literal_eval(data["key"])

        # decrypt aes key
        key = private_key.decrypt(
            key_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        token = ast.literal_eval(raw_token.decode())

        # decrypt the access token
        access_token = decrypt_data(token, key=key)
        access_token = remove_padding(access_token)
        
        # Validate token and retrieve app
        token = self.get_validated_token(access_token)
        
        try:
            app = Application.objects.get(uuid=token['uuid'])
        except Application.DoesNotExist:
            raise AuthenticationFailed('No Application found')

        return (app, token)

    def get_raw_token(self, header: bytes) -> bytes | None:

        return header