from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    lastt_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    conact_picture = models.URLField(null=True)
    is_favourited = models.BooleanField(default=True)
