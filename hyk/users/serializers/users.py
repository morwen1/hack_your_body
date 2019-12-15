#django
#restframework
from rest_framework import serializers
#models
from hyk.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('email' , 'first_name' ,'username')
