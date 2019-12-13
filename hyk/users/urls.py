#django
from django.urls import path , include
#rest_framework
from rest_framework.routers import SimpleRouter
#views
from hyk.users.views import UserViewset ,ProfileViewset

router = SimpleRouter()
router.register(r'' , UserViewset , basename='users_urls')
router.register(r'profile', ProfileViewset , basename='profile_update')
app_name = "users"
urlpatterns = [
    path('' , include(router.urls))
]
