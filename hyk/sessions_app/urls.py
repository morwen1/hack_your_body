#django
from django.urls import path , include
#rest_framework
from rest_framework.routers import SimpleRouter
#views
from hyk.sessions_app.views import SessionsViewset

router = SimpleRouter()
router.register(r'profile/(?P<profile>[0-9]+)/session' , SessionsViewset , basename= 'sessions')


urlpatterns = [
    path('' , include(router.urls))
]
