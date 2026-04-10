from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_member = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username