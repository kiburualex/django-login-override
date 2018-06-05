from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from datetime import date
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import pgettext_lazy
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_staff=False,
                    is_active=True, username='', **extra_fields):
        'Creates a User with the given username, email and password'
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True,
                                is_superuser=True, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(pgettext_lazy('User field', 'email'), unique=True)
    fullname = models.CharField(pgettext_lazy('User field', 'fullname'), unique=True, max_length=100, null=True, blank=True)
    name = models.CharField(pgettext_lazy('User field', 'name'), unique=True, max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(
        pgettext_lazy('User field', 'employee status'),
        default=False)
    is_active = models.BooleanField(
        pgettext_lazy('User field', 'active'),
        default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')


