from django.core.exceptions import ValidationError
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from cyber.auth import ApplicationAuthentication
from cyber.permissions import ApplicationRequiredPermissions

from rest_framework import generics, status
from rest_framework.response import Response

from myadmin.api.serializers import LogAppDateSerializers, LogAppMonthSerializers, LogAppSerializers, LogAppYearSerializers, LogDateSerializers, LogModelDateSerializers, LogModelMonthSerializers, LogModelSerializers, LogModelYearSerializers, LogMonthSerializers, LogSerializer, LogUserDateSerializers, LogUserMonthSerializers, LogUserSerializers, LogUserYearSerializers, LogYearSerializers, ProfileGetSerializer, ProfileSerializer, ProfileUpdateSerializer
from myadmin.models import Profile

class LogView(generics.ListAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogSerializer
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


class LogYearView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogYearSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogMonthView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogMonthSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogDateView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogDateSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogAppView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogAppSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogAppYearView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogAppYearSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)


class LogAppMonthView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogAppMonthSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogAppDateView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogAppDateSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogModelView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogModelSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)


class LogModelYearView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogModelYearSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogModelMonthView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogModelMonthSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogModelDateView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogModelDateSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogUserView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogUserSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)


class LogUserYearView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogUserYearSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogUserMonthView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogUserMonthSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    

class LogUserDateView(generics.GenericAPIView):
    authentication_classes = (ApplicationAuthentication,)
    serializer_class = LogUserDateSerializers
    permission_classes = (ApplicationRequiredPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)


class ProfileUpdateView(generics.UpdateAPIView):
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()
    
    def get_object(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = request.data["user_id"]

        obj = Profile.objects.get(user=user_id)

        return obj
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(request)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance.profile_img = request.data["profile_img"]
        instance.bio = request.data["bio"]
        instance.save()

        LogEntry.objects.log_action(
            user_id=instance.user.pk,
            content_type_id=ContentType.objects.get_for_model(instance).pk,
            object_id=instance.pk,
            object_repr=instance.user.username,
            action_flag=CHANGE)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        data = {"Message": "Profile update successfull"}

        return Response(data)


class ProfileRetrieveView(generics.RetrieveAPIView):
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)
    serializer_class = ProfileGetSerializer
    queryset = Profile.objects.all()

    def get_object(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.data["user"]

        obj = Profile.objects.get(user=user)

        return obj


class ProfileListView(generics.ListAPIView):
    authentication_classes = (ApplicationAuthentication,)
    permission_classes = (ApplicationRequiredPermissions,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
