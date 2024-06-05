from django.db import models

from vendorapp.constants import FIREARM_CHOICES



class vendorAppModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Firearm(vendorAppModel):
    name = models.CharField(max_length=100)
    firearm_type = models.CharField(max_length=50, choices=FIREARM_CHOICES)