from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group, Permission

User = get_user_model()

class AppManager(models.Manager):
    use_in_migrations = True

    def create_app(self, name, public_key, user_id):
        app = self.model(name=name, user=user_id)
        user = User.objects.get(id=user_id)
        if user.is_superuser == False:
            raise ValueError("User must be a superuser.")

        app.public_key = make_password(public_key)
        app.save(using=self._db)
        return app
    
    def change_public_key(self, uuid, old_key, new_key, email, password):
        user = User.objects.get(email)
        
        if not user or user.check_password(password) == False:
            raise ValueError("incorrect email or password.")

        app = self.model(uuid=uuid)

        if app.user != user:
            raise ValueError("user is unauthorized.")
        
        if app.check_password(old_key) == False:
            raise ValueError("incorrect public key.")
        
        app.public_key = make_password(new_key)
        app.save(using=self._db)
        return app


# Create your models here.
class Application(PermissionsMixin):
    name = models.CharField(max_length=1028)
    uuid = models.UUIDField(unique=True, auto_created=True, null=False)
    public_key = models.CharField(max_length=1028)
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

    _public_key = None

    objects = AppManager()

    def set_password(self, raw_key):
        self.public_key = make_password(raw_key)
        self._public_key = raw_key

    def check_password(self, raw_key):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_key):
            self.set_password(raw_key)
            # Password hash upgrades shouldn't be considered password changes.
            self._public_key = None
            self.save(update_fields=["public_key"])

        return check_password(raw_key, self.public_key, setter)

    

    def __str__(self):
        return self.name
    