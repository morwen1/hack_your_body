from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    email = models.EmailField(unique = True )
    REQUIRED_FIELDS = ('username', 'password' , 'first_name')
    USERNAME_FIELD = 'email'

    
    
    

class Profile (models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    weight = models.SmallIntegerField( help_text="weigth in kg",null=True)
    height = models.SmallIntegerField(help_text="height in cms" , null=True)
    imc = models.IntegerField(default=0)
    atlhetic_discipline = models.CharField(max_length=255 , null =True)
    sessions = models.ManyToManyField(to='exercises.Rutine' ,through="exercises.Sessions"  , through_fields = ('session_profile' ,'session_rutines' ))
    
    