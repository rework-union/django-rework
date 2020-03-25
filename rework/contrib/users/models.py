from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import JSONField


class UserManager(BaseUserManager):
    """默认创建用户时需要 email，自己实现的去掉了 email"""
    use_in_migrations = True

    def _create_user(self, username, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username,
                          is_staff=is_staff, is_active=True,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, **extra_fields)


class User(AbstractUser):
    mobile = models.CharField('手机号', max_length=16, default='', db_index=True, blank=True)

    objects = UserManager()
