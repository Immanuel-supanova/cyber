import ast
import base64
from typing import Any, Dict, Optional, Type
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding 


from cyber.models import Application
from cyber.token import ApplicationToken, RefreshToken
from cyber.key import decrypt_data, private_key, public_key, generate_aes_key, encrypt_data, remove_padding

class AppTokenObtainPairSerializer(serializers.Serializer):
    uuid = serializers.CharField(write_only=True)
    public_key = serializers.CharField(write_only=True)
    token_class = RefreshToken


    def get_app(self, uuid):
        if not uuid:
            raise exceptions.ValidationError("uuid is required.")
        
        try:
            app = Application.objects.get(uuid=uuid)
        except ValidationError:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_application"],
                "app does not exist",
            )
        
        if app.is_active == False:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_application"],
                "Application is not active",
            )

        return app
    
    def validate(self, data) -> Dict[Any, Any]:
        enc_uuid = base64.b64decode(data["uuid"])

        # decrypt enc-uuid
        dec_uuid = private_key.decrypt(
            enc_uuid,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        dec_uuid = dec_uuid.decode()
        
        refresh = self.get_token(self.get_app(uuid=dec_uuid))

        # get self.public_key
        app_public_key = serialization.load_pem_public_key(
            data["public_key"].encode(),
            backend=default_backend()
            )
        
        if not app_public_key:
            raise exceptions.ValidationError("public_key is not the key")
        
        refresh_byte = str(refresh).encode()
        access_byte = str(refresh.access_token).encode()

        key = generate_aes_key()
        # encrypt refresh token 
        enc_refresh = encrypt_data(data=refresh_byte, key=key)

        # encrypt access_token
        enc_access = encrypt_data(data=access_byte, key=key)

        # encrypt key
        enc_key = app_public_key.encrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )


        public_key_str = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()

        data = {}
        data["refresh"] = str(enc_refresh)
        data["access"] = str(enc_access)
        data["public_key"] = public_key_str
        data["key"] = str(enc_key)

        return data
    
    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)


class AppRefreshTokenSerializer(serializers.Serializer):
    refresh_token= "refresh"
    public_key = "public_key"
    key = "key"
    token_class: Optional[Type[ApplicationToken]] = RefreshToken
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields[self.refresh_token] = serializers.CharField(write_only=True)
        self.fields[self.public_key] = serializers.CharField(write_only=True)
        self.fields[self.key] = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)
    
    def validate(self, data) -> Dict[Any, Any]:
        key_bytes = ast.literal_eval(data["key"])
        enc_refresh = ast.literal_eval(data["refresh"])

        # decrypt key
        key = private_key.decrypt(
            key_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # decrypt refresh token
        refresh_token = decrypt_data(enc_refresh, key=key)
        refresh_token = remove_padding(refresh_token)

        refresh = refresh_token.decode()
        # validate refresh token

        verify_token = RefreshToken(refresh)
        verify_token.verify()

        uuid = verify_token.payload["uuid"]
        # check if app exists
        try:
            app = Application.objects.get(uuid=uuid)
        except ValidationError:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_application"],
                "app does not exist",
            )
        
        if app.is_active == False:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_application"],
                "Application is not active",
            )

        refresh = self.get_token(app)

        # get self.public_key
        app_public_key = serialization.load_pem_public_key(
            data["public_key"].encode(),
            backend=default_backend()
            )
        
        if not app_public_key:
            raise exceptions.ValidationError("public_key is not the key")
        
        refresh_byte = str(refresh).encode()
        access_byte = str(refresh.access_token).encode()

        key = generate_aes_key()
        
        # encrypt refresh token 
        enc_refresh = encrypt_data(data=refresh_byte, key=key)

        # encrypt access_token
        enc_access = encrypt_data(data=access_byte, key=key)

        # encrypt key
        enc_key = app_public_key.encrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None
            )
        )


        public_key_str = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()

        data = {}
        data["access"] = str(enc_access)
        data["public_key"] = public_key_str
        data["key"] = str(enc_key)

        return data
