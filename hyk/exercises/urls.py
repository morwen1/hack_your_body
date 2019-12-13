#django
from django.urls import path , include
#rest_framework
from rest_framework.routers import SimpleRouter
#views
from hyk.exercises.views import ExercisesViewset

router = SimpleRouter()
router.register(r'' , ExercisesViewset , basename='exercises')
app_name = "exercises"
urlpatterns = [
    path('' , include(router.urls))
]
