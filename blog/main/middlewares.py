from datetime import time
from logging import Logger
import socket
from .models import Logg


class LogMiddleware:
    def __init__(self, get_responses):
        self.get_response = get_responses

    def __call__(self, request):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        path = request.path
        utm = request.GET.get('utm')
        created = time()
        if utm:
            time_exec = time() - created
            utm_log = Logg(utm=utm, time_execution=time_exec, path=path, created=created, user_ip=ip_address)
            utm_log.save()
        response = self.get_response(request)
        return response