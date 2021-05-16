

def notify(email_to):
    telegram_notify(email_to)
    email_send(email_to)


def email_send(email_to):
    from django.core.mail import send_mail
    send_mail(
        'My Blog',
        'You have subscribed on Author: {}'.format('test name'),
        'some@gmail.com',
        [email_to],
        fail_silently=False,
    )


def telegram_notify(email_to):
    pass


def email_send_all(email_to):
    from django.core.mail import send_mail
    send_mail(
        'My Blog',
        'I need to take msg from a link',
        'some@gmail.com',
        [email_to],
        fail_silently=False,
    )
