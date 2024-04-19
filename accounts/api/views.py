from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()


class UserCreate(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = (DjangoModelPermissions,)



class UserList(generics.ListAPIView):
    """
    UserList lists all User entities
    """

    serializer_class = UserSerializer
    queryset = User.objects.exclude(is_superuser=True)
    permission_classes = (DjangoModelPermissions,)


class UserRetrieve(generics.RetrieveAPIView):
    """
    UserRetrieve is used to retrieve individual users from the database
    """

    serializer_class = UserSerializer
    queryset = User.objects.exclude(is_superuser=True)
    permission_classes = (DjangoModelPermissions,)


class CurrentUser(APIView):
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

