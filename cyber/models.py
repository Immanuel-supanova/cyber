import uuid

from django.contrib.auth import get_user_model
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group, Permission

User = get_user_model()

class AppManager(models.Manager):
    use_in_migrations = True

    def create_app(self, name, user):
        app_uuid = uuid.uuid4()
        app = self.model(name=name, user=user, uuid=app_uuid)
        user = User.objects.get(email=user.email)
        if user.is_superuser == False:
            raise ValueError("User must be a superuser.")

        app.save(using=self._db)
        LogEntry.objects.log_action(
            user_id=user.id,
            content_type_id=ContentType.objects.get_for_model(self.model).pk,
            object_id=app.pk,
            object_repr=app.user.username,
            action_flag=ADDITION)
        return app


# Create your models here.
class Application(PermissionsMixin):
    name = models.CharField(max_length=1028)
    uuid = models.UUIDField(unique=True, auto_created=True, null=False)
    is_active = models.BooleanField(default=True)
    is_anonymous = models.BooleanField(default=False)
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
    