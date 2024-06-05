from Authapp.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"

  def create(self, validated_data):
    user = User.objects.create_user(
        validated_data['email'],
        validated_data['user_type'], 
        validated_data['phone'], 
        validated_data['password']
    )
    return user


class AuthSerializer(serializers.Serializer):
    '''serializer for the user authentication object'''
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )    
    def validate(self, attrs):
        email = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        print('here', attrs.username, user.email)
        
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return