#django 
from django.contrib.auth import password_validation , authenticate
#rest_framework
from rest_framework import serializers
from rest_framework.validators  import UniqueValidator
#models 
from hyk.users.models import User , Profile
#serializers 
from hyk.users.serializers import UserSerializer



class SignupSerializer(serializers.Serializer):
    """
    signup serializer create user and create porfile 
    """
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name= serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    password_verif = serializers.CharField(max_length=100)


    def validate(self , data):
        #import pdb; pdb.set_trace()
        password = data['password'] 
        password_verif = data['password_verif']
        if password != password_verif :
            raise serializers.ValidationError('passwords does not equals')
        else: 
            password_validation.validate_password(password)
        return data
    

    def create(self , data) : 
        data.pop('password_verif')
        #import pdb; pdb.set_trace()
        user = User.objects.create_user(**data)
        user.save()
        Profile.objects.create(user=user)
        return user

        