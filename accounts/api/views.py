from django.contrib.auth import get_user_model
from rest_framework import generics, status
from django.core.exceptions import ValidationError
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import PasswordResetSerializer, UserSerializer, RegisterSerializer

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

class UserPasswordReset(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    