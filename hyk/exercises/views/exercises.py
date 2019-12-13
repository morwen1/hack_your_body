
# django

from django.db.models import Prefetch
# rest_framework

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# serializers
from hyk.exercises.serializers import ExercisesSerializer ,ExercisesSerializerCreate ,ProfileSerializer
# models
from hyk.exercises.models import Exercises
from hyk.users.models import Profile


class ExercisesViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):





    def get_serializer_class(self):

        if self.action in ['create' , 'update' , 'partial_update']:
            serializer = ExercisesSerializerCreate
        if self.action in ['list' ,'retrieve'] :
            serializer = ExercisesSerializer

        return serializer


    def get_queryset(self):
        queryset = []
        if self.action in ['list' , 'retrieve']:
            queryset = Exercises.objects.all()
        if self.action in ['update', 'partial_update','create']:
            user = self.request.user
            profile = Profile.objects.get(user=user)
            queryset = Exercises.objects.filter(created_of=profile)
        if queryset != []:
            queryset.prefetch_related(Prefetch('instructions'))
        #import pdb; pdb.set_trace()
        return queryset

    def get_permissions(self):
        permissions = []
        if self.action == 'list':
            permissions = [AllowAny]
        if self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'profile':Profile.objects.get(user=self.request.user),
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }