from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# The target is to login with email rather than username
class User(AbstractUser):
    pass
