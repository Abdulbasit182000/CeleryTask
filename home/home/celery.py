from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")
app = Celery("home")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
   "convert_utc": {
       "task": "app.tasks.convert_utc",
       "schedule": 10,
   },
   "convert_pst": {
       "task": "app.tasks.convert_pst",
       "schedule": 10,
   },
}


app.autodiscover_tasks()
