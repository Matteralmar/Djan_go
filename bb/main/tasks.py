
from celery import shared_task

from .models import Subscriber
from .notify_service import email_send, email_send_all


@shared_task
def notify_async(email_to):
    print("---- tasks: smth_slow_async - START")
    email_send(email_to)
    print("---- tasks: smth_slow_async - END")


@shared_task
def notify_async_all():
    all_emails = Subscriber.objects.all().values('email_to')
    print("---- tasks: smth_slow_async - START")
    email_send_all(all_emails)
    print("---- tasks: smth_slow_async - END")