from rest_framework import serializers
from hyk.exercises.models import Info_Sessions

class Info_sessions (serializers.ModelSerializer):
    class Meta:
        model= Info_Sessions
        fields = '__all__'