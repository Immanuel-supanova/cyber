from django.core.exceptions import ValidationError
from django.contrib.admin.models import LogEntry

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions

from myadmin.api.serializers import LogAppDateSerializers, LogAppMonthSerializers, LogAppSerializers, LogAppYearSerializers, LogDateSerializers, LogModelDateSerializers, LogModelMonthSerializers, LogModelSerializers, LogModelYearSerializers, LogMonthSerializers, LogSerializer, LogUserDateSerializers, LogUserMonthSerializers, LogUserSerializers, LogUserYearSerializers, LogYearSerializers

class LogView(generics.ListAPIView):
    serializer_class = LogSerializer
    permission_classes = (DjangoModelPermissions,)
    queryset = LogEntry.objects.all()


class LogYearView(generics.GenericAPIView):
    serializer_class = LogYearSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogMonthSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogDateSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogAppSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogAppYearSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogAppMonthSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogAppDateSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogModelSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogModelYearSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogModelMonthSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogModelDateSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogUserSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogUserYearSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogUserMonthSerializers
    permission_classes = (DjangoModelPermissions,)
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
    serializer_class = LogUserDateSerializers
    permission_classes = (DjangoModelPermissions,)
    queryset = LogEntry.objects.all()


    def post(self, request, *args, **kwargs):
        # Accessing data from POST request
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError(e.args[0])
        
        return Response({"message": serializer.validated_data}, status=status.HTTP_200_OK)
    