#restframework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin , ListModelMixin , RetrieveModelMixin
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
#serializers
from hyk.information.serializers.info_sessions import Info_sessions_Serializer

#models
from hyk.information.models import Info_Sessions
from hyk.exercises.models import Sessions





class SessionInfoViewset(
    UpdateModelMixin ,
    RetrieveModelMixin, 
    ListModelMixin , 
    GenericViewSet):
    
    """
        Edit only the information of the sessions
    """


    def dispatch(self, request,*args , **kwargs):
        self.session = get_object_or_404(Sessions , id=int(kwargs['id_session']))
        return super(SessionInfoViewset , self).dispatch(request, *args, **kwargs)
    
    permission_classes = [IsAuthenticated]
    serializer_class = Info_sessions_Serializer
    def get_queryset(self):
        if self.session.session_profile.user == self.request.user:
            queryset = Info_Sessions.objects.filter(id=self.session.info_session.id)
        else :
            queryset = []
        return queryset
    

    