from django.shortcuts import render
from django.db import transaction
from Authapp.models import User
from clientapp.models import ClientApplication, ClientFirearm, ClientProfile
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from clientapp.serializer import ClientApplicationViewSerializer, ClientFirearmSerializer, ClientProfileSerializer


class ClientProfileView(viewsets.ViewSet):
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_profile(self, request):
        user = request.user
        client = ClientProfile.objects.filter(user=user).first()
        if client:
            serializer = self.serializer_class(client, many=False)
            return Response({'data':serializer.data}, status=200)
        else:
            return Response({"error": 'No such client'}, status=500)
        
        
    def update(self, request):
        data = request.data
        user = request.user
        client = ClientProfile.objects.filter(user=user).first()
        if client:
            serializer = self.serializer_class(client, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data':serializer.data}, status=200)
        else:
            return Response({"error": 'No such client'}, status=500)


# Client applications
class ClientApplicationView(viewsets.ViewSet):
    serializer_class = ClientApplicationViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    # get client applications 
    def get_applications(self, request):
        try:
            user = request.user        
            client = ClientProfile.objects.filter(user=user).first()
            clientApplications = ClientApplication.objects.filter(client=client)
            if clientApplications:
                serializer = self.serializer_class(clientApplications, many=True)
                return Response({'message': 'succes', "data":serializer.data}, status=200)                
            else:
                return Response({'message':"No Applications found"}, status=400)  
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    # client application 
    def create(self, request):
        try:
            with transaction.atomic():                
                user = request.user    
                print('user', user, User.objects.count())   

                client = ClientProfile.objects.filter(user__id=user).first()
                if client:
                    data = request.data
                    data['client'] = client.id
                    serializer = self.serializer_class(data=data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response({'message': 'success', 'succcess': True, data:serializer.data}, status=201)
                else:
                    return Response({'message':"No such client"}, status=400)
            
        except Exception as e:
            return Response({"error": str(e), 'success': False}, status=500)


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
        
