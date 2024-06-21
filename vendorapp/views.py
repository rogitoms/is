from django.shortcuts import render
from django.shortcuts import render
from django.db import transaction
from Authapp.models import User
from clientapp.models import ClientApplication, ClientFirearm, ClientProfile
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from clientapp.serializer import ClientApplicationViewSerializer, ClientFirearmSerializer, ClientProfileSerializer

# Client firearms
class ClientFirearmsView(viewsets.ViewSet):
    serializer_class = ClientFirearmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_client_firearms(self, request):
        try:
            user = request.user   
            client = ClientProfile.objects.filter(user=user).first()     
            firearms = ClientFirearm.objects.filter(client=client)
            if firearms:
                serializer = self.serializer_class(ClientFirearm, many=True)
                return Response({'message': 'succes', "data":serializer.data}, status=200)                
            else:
                return Response({'message':"No Firearms found"}, status=200)  
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def details(self, request):
        try:
            user = request.user        
            client = ClientProfile.objects.filter(user=user).first()
            firearms = ClientFirearm.objects.filter(client=client)
            if firearms:
                serializer = self.serializer_class(ClientFirearm, many=True)
                return Response({'message': 'succes', "data":serializer.data}, status=200)                
            else:
                return Response({'message':"No Firearms found"}, status=200) 
            
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

