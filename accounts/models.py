from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")

    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'  # Use email for authentication
    # REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
