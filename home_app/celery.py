from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home_app.settings")

app = Celery("home_app")
app.conf.update(timezone="Asia/Kolkata")
app.config_from_object(settings, namespace="CELERY")

# Celery Beat Settings

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Task by Shiyas {self.request}")
