from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExercisesConfig(AppConfig):
    name = "exercises"
    verbose_name = _("Exercises")


    