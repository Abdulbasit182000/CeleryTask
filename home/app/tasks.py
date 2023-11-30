from django.utils.crypto import get_random_string
from celery import shared_task
from datetime import timedelta
from celery import Celery
from faker import Faker
from . models import Person,CustomUser
from django.utils import timezone
import logging
import pytz

logger = logging.getLogger(__name__)

@shared_task
def convert(start, end):
    x = CustomUser.objects.all()
    
    while start != end:
        if x[start].is_staff == 'True':
            end += 1
        else:
            logger.info(x[start].date_of_birth)
            start += 1

@shared_task
def convertpst(start, end):
    x = CustomUser.objects.all()
    
    while start != end:
        if x[start].is_staff == 'True':
            end += 1
        else:
            date_of_birth = x[start].date_of_birth

            # Check if date_of_birth is not None before making it aware
            if date_of_birth is not None:
                 w_pst = date_of_birth.astimezone(timezone.get_fixed_timezone(-480))  # UTC-8 (PST)
                 logger.info(w_pst)
                
            start += 1






# @shared_task
# def utc_convert(start,end):     #for UTC
#     x=CustomUser.objects.all()
#     while(start!=end):
#         if x[start].is_staff=='True':
#             end+1
#         else:
#             logger.info(f'pst {x[start].email}:{x[start].date_of_birth}')
#             x[start].date_of_birth=timezone.make_aware(x[start].date_of_birth,timezone='UTC')
#             logger.info(f'utc {x[start].email}:{x[start].date_of_birth}')
#             x[start].save()
#         start+1

# @shared_task
# def pst_convert(start,end):     #for PST
#     x=CustomUser.objects.all()
#     while(start!=end):
#         if x[start].is_staff=='True':
#             end+1
#         else:
#             logger.info(f'utc {x[start].email}:{x[start].date_of_birth}')
#             x[start].date_of_birth=timezone.make_aware(x[start].date_of_birth,timezone=timezone.get_current_timezone())
#             logger.info(f'pst {x[start].email}:{x[start].date_of_birth}')
#             x[start].save()
#         start+1

# while(True):
#     start = 0
#     end = 10
#     a=True
#     while(a):   #To UTC
#         logger.info('converstion to utc started')
#         x=CustomUser.objects.all()
#         if(start==len(x)):
#             a=False
#         if(end>len(x)):
#             end=len(x)
#         utc_convert.apply_async(args=[start,end],countdown=10)
#         start=end
#         end = end+10

#     start = 0
#     end = 10
#     a=True

#     while(a):    #To PST
#         x=CustomUser.objects.all()
#         logger.info('converstion to pst started')
#         if(start==len(x)):
#             a=False
#         if(end>len(x)):
#             end=len(x)
#         x=pst_convert.apply_async(args=[start,end],countdown=10)
#         start=end
#         end = end+10
