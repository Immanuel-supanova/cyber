from rest_framework.permissions import DjangoModelPermissions

class ApplicationRequiredPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):
        # Assuming ApplicationAuthentication provides (app, token)
        app, token = request.auth

        # Check if the authenticated app has the required permissions
        if not app:
            return False
        
        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return app.has_perms(perms)