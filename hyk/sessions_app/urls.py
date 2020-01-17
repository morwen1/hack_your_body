#django
from django.urls import path , include
#rest_framework
from rest_framework.routers import SimpleRouter
#views
from hyk.sessions_app.views import SessionsViewset , SessionInfoViewset

router = SimpleRouter()

router.register(r'profile/(?P<profile>[0-9]+)/session' , SessionsViewset , basename= 'sessions')
router.register(r'session/(?P<id_session>[0-9]+)/info' , SessionInfoViewset , basename= 'sessions_information')


urlpatterns = [
    path('' , include(router.urls))
]
