#django rest framework
from rest_framework import mixins , viewsets
from rest_framework.permissions import IsAuthenticated , AllowAny
#serializer 
from hyk.users.serializers import ProfileSerializer , ProfileSerializerCreate

#models 
from hyk.users.models import Profile



class ProfileViewset(
    mixins.UpdateModelMixin , 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):


    def get_serializer_class (self):
        if self.action == 'list':
            serializer = ProfileSerializer
        if self.action in ['update' , 'partial_update']:
            serializer = ProfileSerializerCreate
        return serializer

    def get_queryset (self):
        queryset = []
        if self.action == 'list':
            queryset = Profile.objects.all()
        if self.action in ['update' , 'partial_update']:
            user = self.request.user
            queryset = Profile.objects.filter(user=user)
        return queryset

    def get_permissions(self):
        permissions = [] 
        if self.action == 'list':
            permissions = [AllowAny]
        if self.action in ['update' , 'partial_update']:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]
