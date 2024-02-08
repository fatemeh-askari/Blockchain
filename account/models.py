from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name='mobile number')
    email_active_code = models.CharField(max_length=400, verbose_name='email activation code')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_full_name()
