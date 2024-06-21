from django.db import models

from vendorapp.constants import FIREARM_CHOICES,AMMUNITION_TYPE,AMMUNITION_CALIBER,FIREARM_CONDITION 



class vendorAppModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Firearm(vendorAppModel):
    name = models.CharField(max_length=100)
    firearm_type = models.CharField(max_length=50, choices=FIREARM_CHOICES)
    condition = models.CharField(max_length=20, choices=FIREARM_CONDITION, blank=True, null=True)
   
    
class Ammunition(vendorAppModel):
    caliber = models.CharField(max_length=20, choices=AMMUNITION_CALIBER, blank=True, null=True)
    ammunition_type = models.CharField(max_length=20, choices=AMMUNITION_TYPE, blank=True, null=True)
    
    