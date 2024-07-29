import time

from celery import shared_task


@shared_task
def simple_task():
    time.sleep(10)
