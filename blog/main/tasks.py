import datetime

from celery import shared_task

from django.utils import timezone

from .models import Subscriber, Logg
from .notify_service import email_send


@shared_task
def notify_async(email_to):
    print("---- tasks: smth_slow_async - START")
    email_send(email_to)
    print("---- tasks: smth_slow_async - END")


# @shared_task
# def notify_async_all():
# all_emails = Subscriber.objects.all().values('email_to')
# for email in all_emails:
# email_send_all(email)


def delete_old_logs():
    logs = Logg.objects.all()
    for log in logs:
        if log.created < timezone.now() - datetime.timedelta(days=3):
            log.delete()
