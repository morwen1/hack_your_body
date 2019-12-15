#django
from django.contrib.auth import authenticate 
#rest_framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
#serializers 
from hyk.users.serializers import UserSerializer
#models
from hyk.users.models import  Profile , User




class LoginSerializer (serializers.Serializer):
    """
    Serializers of signin user 
    and authenticate in the sistem

    """
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self ,data ):
        user = authenticate(email = data['email'] , password = data['password'])
        if not user:
            raise serializers.ValidationError('username or password is invalid')
        else:
            self.context['user'] = user
            return data

    def create(self,data):
        token , created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'] , token.key