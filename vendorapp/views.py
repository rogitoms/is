from django.shortcuts import render
from django.shortcuts import render
from django.db import transaction
from Authapp.models import User
from clientapp.models import ClientFirearm, ClientProfile
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from clientapp.serializer import ClientFirearmSerializer
from vendorapp.models import Firearm
from vendorapp.serializer import FirearmSerializer

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
        
        #vendor see firearms
class FirearmViewSet(viewsets.ViewSet):
    
    def list_firearms(self, request):
        firearms = Firearm.objects.all()
        serializer = FirearmSerializer(firearms, many=True)
        return Response(serializer.data)

    def retrieve_firearm(self, request, id=None):
        try:
            firearm = Firearm.objects.get(pk=id)
        except Firearm.DoesNotExist:
            return Response(status=404)
        
        serializer = FirearmSerializer(firearm)
        return Response(serializer.data)

    def create_firearm(self, request):
        serializer = FirearmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=401)
