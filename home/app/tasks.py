import logging
from datetime import timedelta

import redis
from celery import shared_task

from .models import CustomUser

logger = logging.getLogger(__name__)


@shared_task
def convert_utc():
    redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
    users = CustomUser.objects.exclude(is_superuser=True)
    users = users.exclude(is_changed=True)
    if len(users) == 0:
        redis_client.set("key", 0)
    if len(users) != 0 and (int(redis_client.get("key"))) == 1:
        count = 0
        for user in users:
            user.date_of_birth = user.date_of_birth + timedelta(hours=8)
            user.is_changed = True
            user.save()
            count = count + 1
            if count == 10:
                break
    else:
        users = CustomUser.objects.exclude(is_superuser=True)
        users = users.exclude(is_changed=False)
        if len(users) == 0:
            redis_client.set("key", 1)
        count = 0
        for user in users:
            user.date_of_birth = user.date_of_birth - timedelta(hours=8)
            user.is_changed = False
            user.save()
            count = count + 1
            if count == 10:
                break
