from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Email is required to create users by default, and
    the implementation here removes the email
    """
    use_in_migrations = True

    def _create_user(self, username, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=username, is_staff=is_staff, is_active=True, date_joined=now, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, **extra_fields)


class EnhancedAbstractUser(AbstractUser):
    mobile = models.CharField(_('mobile'), max_length=16, default='', db_index=True, blank=True)
    nickname = models.CharField(_('nickname'), max_length=128, default='')
    avatar = models.CharField(_('avatar'), max_length=256, default='')

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True
