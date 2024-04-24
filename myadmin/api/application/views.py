from django.core.exceptions import ValidationError
from django.contrib.admin.models import LogEntry

from cyber.auth import ApplicationAuthentication
from cyber.permissions import ApplicationRequiredPermissions

from rest_framework import generics, status
from rest_framework.response import Response

from myadmin.api.serializers import LogAppDateSerializers, LogAppMonthSerializers, LogAppSerializers, LogAppYearSerializers, LogDateSerializers, LogModelDateSerializers, LogModelMonthSerializers, LogModelSerializers, LogModelYearSerializers, LogMonthSerializers, LogSerializer, LogUserDateSerializers, LogUserMonthSerializers, LogUserSerializers, LogUserYearSerializers, LogYearSerializers

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
    