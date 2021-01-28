from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    GROUP_CHOICES = (
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three')
    )

    is_superuser = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_group     = models.CharField(max_length=20, choices=GROUP_CHOICES)
