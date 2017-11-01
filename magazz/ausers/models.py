from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# Create your models here.


class User(AbstractUser, models.Model):
    pass


