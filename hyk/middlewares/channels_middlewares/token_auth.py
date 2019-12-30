from rest_framework.authtoken.models import Token
from django.db import close_old_connections




class Channels_Token_Auth:

    def __init__(self,inner):
        self.inner = inner 
    

    def  __call__(self , scope):
        close_old_connections()
        token = scope["query_string"].decode()
        user = Token.objects.get(key = token).user
        return self.inner ( dict(scope , user=user))