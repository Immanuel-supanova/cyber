from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group, Permission

User = get_user_model()

class AppManager(models.Manager):
    use_in_migrations = True

    def create_app(self, name, user_id):
        app = self.model(name=name, user=user_id)
        user = User.objects.get(id=user_id)
        if user.is_superuser == False:
            raise ValueError("User must be a superuser.")

        app.save(using=self._db)
        return app


# Create your models here.
class Application(PermissionsMixin):
    name = models.CharField(max_length=1028)
    uuid = models.UUIDField(unique=True, auto_created=True, null=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="app_user")
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="app_set",
        related_query_name="app",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="app_set",
        related_query_name="app",
    )

    objects = AppManager()

    def __str__(self):
        return self.name
    