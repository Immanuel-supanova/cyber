from django.contrib.auth import get_user_model
from rest_framework import generics, status
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from accounts.api.serializers import PasswordResetSerializer, RegisterSerializer, UserSerializer
from cyber.auth import ApplicationAuthentication
from cyber.permissions import ApplicationRequiredPermissions

User = get_user_model()

# Application 
class AppUserCreate(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)



class AppUserList(generics.ListAPIView):
    """
    UserList lists all User entities
    """

    serializer_class = UserSerializer
    queryset = User.objects.exclude(is_superuser=True)
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)


class AppUserRetrieve(generics.RetrieveAPIView):
    """
    UserRetrieve is used to retrieve individual users from the database
    """

    serializer_class = UserSerializer
    queryset = User.objects.exclude(is_superuser=True)
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)


class AppUserPasswordReset(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    