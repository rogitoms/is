from django.db import models
from vendorapp.constants import FIREARM_CHOICES,AMMUNITION_TYPE,AMMUNITION_CALIBER,FIREARM_CONDITION 

class vendorAppModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Firearm(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    caliber = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.type} ({self.caliber})"
   
    