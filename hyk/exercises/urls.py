#django
from django.urls import path , include
#rest_framework
from rest_framework.routers import SimpleRouter
#views
from hyk.exercises.views import ExercisesViewset , RutineViewset

router = SimpleRouter()
router.register(r'exercises' , ExercisesViewset , basename='exercises')
router.register(r'rutines' , RutineViewset , basename='rutine')
app_name = "exercises"
urlpatterns = [
    path('' , include(router.urls))
]
