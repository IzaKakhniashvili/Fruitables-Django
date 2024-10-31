from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_active_datetime = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def update_last_active(self):
        self.last_active_datetime = timezone.now()
        self.save()

    def __str__(self):
        return self.username
