# serializers.py
from rest_framework import serializers
from .models import Firearm

class FirearmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firearm
        fields = ['id', 'name', 'type', 'caliber']
