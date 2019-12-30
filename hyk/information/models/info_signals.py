from django.db.models.signals import  pre_save

from django.dispatch import receiver





@receiver(pre_save, sender='exercises.Sessions' , dispatch_uid="update_time_info" )
def update_time_info(sender ,**kwargs):
    """
    obtengo la duracion de la session y 
    la asigno a la tabla de informacion para mejor manejo de info
    """
    session = kwargs['instance']
    if session.info_session.id :
        session.info_session.time = session.duration
        session.info_session.save()

