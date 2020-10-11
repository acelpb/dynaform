from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    image = models.ImageField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    copyright_holder = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
