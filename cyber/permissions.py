from rest_framework.permissions import DjangoModelPermissions

from cyber.models import Application

class ApplicationRequiredPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):

        token = request.auth

        if not token:
            return False
        
        uuid = token["uuid"]
        app = Application.objects.get(uuid=uuid)
        
        if not app:
            return False
        
        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return app.has_perms(perms)