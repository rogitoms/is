from django.db import models
from clientapp.constants import APPLICATION_STATUS, ARMED_STATUS, FILETAGS


class clientAppModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClientProfile(clientAppModel):
    user = models.OneToOneField('Authapp.User', on_delete=models.CASCADE, related_name="client_profile")
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30,blank=True, null=True)
    ID_Number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    
class ClientDocuments(clientAppModel):
    client = models.ForeignKey('clientapp.ClientProfile', on_delete=models.CASCADE, related_name="Client_documents")
    file = models.FileField(upload_to="client/profile")
    tag = models.CharField(max_length=20, choices=FILETAGS)


class ClientApplication(clientAppModel):
    client = models.ForeignKey('clientapp.ClientProfile', on_delete=models.CASCADE, related_name="Client_application")
    next_of_kin_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    reason = models.TextField()
    type_of_firearm = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending", choices=APPLICATION_STATUS)

    
class ClientFirearm(clientAppModel):
    client = models.ForeignKey('clientapp.ClientProfile', on_delete=models.CASCADE, related_name="client_firearm")
    firearm = models.ForeignKey('vendorapp.Firearm', on_delete=models.CASCADE, related_name="client_assigned_firearm")
    status = models.CharField(max_length=20, choices=ARMED_STATUS)


    

