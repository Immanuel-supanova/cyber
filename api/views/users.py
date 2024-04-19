from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from accounts.api.serializers import RegisterSerializer, UserSerializer
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