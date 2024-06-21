from Authapp.models import User
from clientapp.models import ClientApplication, ClientFirearm, ClientProfile
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = User.objects.filter(id=instance.user.id).first()
        rep['user_email'] = user.email
        rep['user_password'] = user.password

        return rep


class ClientApplicationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientApplication
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['client'] = ClientProfileSerializer().data

        return rep


class ClientFirearmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFirearm
        fields = '__all__'