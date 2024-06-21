from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from clientapp.models import ClientProfile
from clientapp.serializer import ClientProfileSerializer


class ClientView(viewsets.ViewSet):
    serializer_class = ClientProfileSerializer

    # List all clients
    def list(self, request):
        clients = ClientProfile.objects.all()
        serializer = self.serializer_class(clients, many=True)
        return Response({'data':serializer.data, 'success':True}, status=200)
    


