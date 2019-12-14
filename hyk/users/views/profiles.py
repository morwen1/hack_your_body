
# django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# serializer
from hyk.users.serializers import ProfileSerializer, ProfileSerializerCreate , ProfileSerializerALL
from hyk.exercises.serializers import ProfileAddRutineSerializer
# models
from hyk.users.models import Profile
from hyk.exercises.models import Rutine


class ProfileViewset(
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            serializer = ProfileSerializer
        if self.action in ['update', 'partial_update']:
            serializer = ProfileSerializerCreate
        return serializer

    def get_queryset(self):
        queryset = []
        if self.action == 'list':
            queryset = Profile.objects.all()
        if self.action in ['update', 'partial_update']:
            user = self.request.user
            queryset = Profile.objects.filter(user=user)
        return queryset

    def get_permissions(self):
        permissions = []
        if self.action == 'list':
            permissions = [AllowAny]
        if self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def add_rutines(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileAddRutineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rutine = Rutine.objects.get(id=request.data['rutine'])
        profile.rutines.add(rutine)

        return Response(data=ProfileSerializerALL(profile).data)

    @action(detail=False,methods=['post'])
    def remove_rutines(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileAddRutineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rutine = Rutine.objects.get(id=request.data['rutine'])
        profile.rutines.remove(rutine)

        return Response(data=ProfileSerializer(profile).data)
