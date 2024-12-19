import os
import django
import datetime
from django.utils.timezone import localtime
from timer import get_duration, format_duration


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit # noqa: E402
from datacenter.models import is_visit_long


if __name__ == '__main__':
    passcard = Passcard.objects.get(owner_name="Breanna Campbell")
    this_passcard_visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)

    long_visits = []
    for visit in this_passcard_visits:
        entered_at = visit.entered_at
        duration_visit_in_minutes = int(get_duration(visit).total_seconds() // 60)

        if is_visit_long(duration_visit_in_minutes, minutes=50):
            print(visit)
        if is_visit_long(duration_visit_in_minutes, minutes=1000):
            print(visit)











        
            
           


        


       








    
    




   


   

