from typing import Any, Dict, Optional, Type
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from cyber.models import Application
from cyber.token import ApplicationToken, RefreshToken, AccessToken

class AppTokenObtainPairSerializer(serializers.Serializer):
    uuid = serializers.CharField(write_only=True)
    # public_key = serializers.CharField(write_only=True)
    token_class = RefreshToken


    def get_app(self, data):
        if "uuid" not in data:
            raise exceptions.ValidationError("uuid is required.")
        
        try:
            app = Application.objects.get(uuid=data["uuid"])
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
        refresh = self.get_token(self.get_app(data=data))
        # get self.public_key
        # encrypt refresh token
        # encrypt access_token
        data = {}
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    
    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)


    
    
class AppRefreshTokenSerializer(serializers.Serializer):
    refresh_token= "refresh"
    # public_key = "key"
    token_class: Optional[Type[ApplicationToken]] = RefreshToken
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields[self.refresh_token] = serializers.CharField(write_only=True)
        # self.fields[self.public_key] = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)
    
    def validate(self, data) -> Dict[Any, Any]:
        # get rsa private key
        # decrypt refresh token
        # validate refresh token

        verify_token = RefreshToken(data["refresh"])
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

        data = {}

        refresh = self.get_token(app)
        # get self.public_key
        # encrypt access_token
        data["access"] = str(refresh.access_token)

        return data

