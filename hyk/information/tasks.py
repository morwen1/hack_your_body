from celery.decorators import periodic_task
from datetime import timedelta
#models
from hyk.information.models import Info_Month , Info_Sessions 
from hyk.users.models import Profile


"""

@periodic_task(name='moth_sessions_information' , run_every=timedelta(minutes=2))
def moth_sessions_information():
    
    
    Info_Sessions.objects.filter(Q(created__lte=datetime.datetime.now()) & Q(
    ...: created__gt=datetime.datetime.now()-datetime.timedelta(days=30))) 

"""