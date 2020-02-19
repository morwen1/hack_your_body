
#djang_restframework 
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

#serializers
from hyk.users.serializers import UserSerializer , LoginSerializer , SignupSerializer

#models
from hyk.users.models import Profile, User 




class UserViewset(GenericViewSet):
    """
    Login
        methods : POST
        return: token and user
    
    Signup(register user) :
        methods : Post 
        return : user registered

    """
    def get_serializer_class (self ):
        if self.action == 'login' :
            serializer = LoginSerializer
        if self.action == 'signup':
            serializer = SignupSerializer
        return serializer





    @action(detail=False , methods=['post'])
    def signup(self , request):

        get_serializer  = self.get_serializer_class()
        serializer = get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data ,200)


    @action(detail=False , methods = ['post'])
    def login(self , request):

        get_serializer  = self.get_serializer_class()
        serializer=get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user , token =serializer.save()
        data = {
            'user' : UserSerializer(user).data ,
            'token':token
            }

        return Response( data , status = 201)

    
