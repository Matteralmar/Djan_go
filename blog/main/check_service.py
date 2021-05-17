from django.shortcuts import redirect
from .tasks import notify_async
from .forms import SubscriberForm


def subscribe_check(err, request):
    subscribe_success = False
    email_to = request.POST.get('email_to')
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            subscribe_success = True
        else:
            err = "Error: fail to subscribe"
    else:
        form = SubscriberForm()
    if subscribe_success:
        notify_async.delay(email_to)

    context = {
        'form': form,
        'error': err,

    }
    return context


def day_check():
    pass
