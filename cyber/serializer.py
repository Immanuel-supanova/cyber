from typing import Any, Dict, Optional, Type
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from cyber.models import Application
from cyber.token import ApplicationToken, RefreshToken, AccessToken

class ApplicationTokenSerializer(serializers.Serializer):
    appuuid_field = "uuid"
    public_key = "key"
    token_class: Optional[Type[ApplicationToken]] = None
    
    default_error_messages = {
        "no_active_application": "No active application found with the given credentials"
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields[self.appuuid_field] = serializers.CharField(write_only=True)
        self.fields[self.public_key] = serializers.CharField(write_only=True)

    def validate(self, data) -> Dict[Any, Any]:
        
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

        return {}

    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)

class ApplicationTokenObtainPairSerializer(ApplicationTokenSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.app)
        # get self.public_key
        # encrypt refresh token
        # encrypt access_token
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    
class ApplicationRefreshTokenSerializer(serializers.Serializer):
    refresh_token= "refresh"
    public_key = "key"
    token_class: Optional[Type[ApplicationToken]] = AccessToken
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields[self.refresh_token] = serializers.CharField(write_only=True)
        self.fields[self.public_key] = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, app: Application):
        return cls.token_class.for_user(app)
    
    def validate(self, data) -> Dict[Any, Any]:
        # get rsa private key
        # decrypt refresh token
        # validate refresh token

        verify_token = RefreshToken(self.refresh_token)
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

        refresh = self.get_token(self.app)
        # get self.public_key
        # encrypt access_token
        data["access"] = str(refresh.access_token)

        return data

