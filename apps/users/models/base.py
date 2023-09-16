from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from link_chaincloak_django.storage_backends import MediaStorage
from link_chaincloak_django.storage_backends.media_storage import BASE_MEDIA_LOCATION

avatar_storage = MediaStorage(location=f"{BASE_MEDIA_LOCATION}/users/avatars")


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_("first name"), max_length=64, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("last name"), max_length=64, null=True, blank=True)
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        null=True,
        blank=True,
        max_length=16,
    )
    email = models.EmailField(verbose_name=_("email address"), null=True, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name=_("profile picture"),
        storage=avatar_storage,
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if not self.first_name and not self.last_name:
            return None
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return _(f"{self.full_name if self.full_name else self.username}")
