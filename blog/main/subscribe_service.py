from django.core.exceptions import ObjectDoesNotExist

from .models import Subscriber


def subscribe(author_id, email_to):
    try:
        # TODO get Subscriber
        author = Subscriber.objects.get(email_to=email_to, author=author_id)
        return author
    except ObjectDoesNotExist:
        subscriber = Subscriber(email_to=email_to, author=author_id)
        subscriber.save()
        # TODO save Subscriber
