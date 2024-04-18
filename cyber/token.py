from rest_framework_simplejwt.tokens import Token, BlacklistMixin
from rest_framework_simplejwt.settings import api_settings
from cyber.models import Application

class ApplicationToken(Token):
    @classmethod
    def for_user(cls, app: Application) -> "Token":
        """
        Returns an authorization token for the given application that will be provided
        after authenticating the apps' credentials.
        """
        app_uuid = getattr(app, "uuid")

        if not isinstance(app_uuid, str):
            app_uuid= str(app_uuid)

        token = cls()
        token["uuid"] = app_uuid

        return token
    
class AccessToken(ApplicationToken):
    token_type = "access"
    lifetime = api_settings.ACCESS_TOKEN_LIFETIME


class RefreshToken(BlacklistMixin, ApplicationToken):
    token_type = "refresh"
    lifetime = api_settings.REFRESH_TOKEN_LIFETIME
    no_copy_claims = (
        api_settings.TOKEN_TYPE_CLAIM,
        "exp",
        # Both of these claims are included even though they may be the same.
        # It seems possible that a third party token might have a custom or
        # namespaced JTI claim as well as a default "jti" claim.  In that case,
        # we wouldn't want to copy either one.
        api_settings.JTI_CLAIM,
        "jti",
    )
    access_token_class = AccessToken

    @property
    def access_token(self) -> AccessToken:
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        access = self.access_token_class()

        # Use instantiation time of refresh token as relative timestamp for
        # access token "exp" claim.  This ensures that both a refresh and
        # access token expire relative to the same time if they are created as
        # a pair.
        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access