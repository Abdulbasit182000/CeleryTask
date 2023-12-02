import logging
from datetime import timedelta

import redis
from celery import shared_task

from .models import CustomUser

logger = logging.getLogger(__name__)


@shared_task
def convert_utc():
    users = CustomUser.objects.exclude(is_superuser=True, is_changed=True)
    redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
    if len(users) != int(redis_client.get("num")):
        return 0
    else:
        redis_client.set("num", int(redis_client.get("num")) - 10)
        if int(redis_client.get("num")) == 0:
            redis_client.set("num", 100)
        count = 0
        for user in users:
            logger.info(f"before:{user.date_of_birth}")
            user.date_of_birth = user.date_of_birth + timedelta(hours=8)
            user.is_changed = True
            user.save()
            logger.info(f"after:{user.date_of_birth}")
            count = count + 1
            if count == 10:
                break


@shared_task
def convert_pst():
    users = CustomUser.objects.exclude(is_superuser=True, is_changed=False)
    redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
    if len(users) != int(redis_client.get("nums")):
        return 0
    else:
        redis_client.set("nums", int(redis_client.get("nums")) - 10)
        if int(redis_client.get("nums")) == 0:
            redis_client.set("nums", 100)
        count = 0
        for user in users:
            user.date_of_birth = user.date_of_birth - timedelta(hours=8)
            user.is_changed = False
            user.save()
            count = count + 1
            if count == 10:
                break
