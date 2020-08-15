from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = ((GENDER_MALE, "남자"), (GENDER_FEMALE, "여자"))

    avatar = models.ImageField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True)
    bio = models.TextField(default="")

