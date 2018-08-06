import re
from datetime import datetime
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from app.models import User_ticket


class Memiddlewear(MiddlewareMixin):
    def process_request(self,request):
        urls = ['/app/register/', '/app/login/', '/app/index/(\d+)', '/app/list/(\d+)/',
                '/app/detail/(\d+)/']

        path = request.path

        for url in urls:
            if re.match(url,path):
                return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('user:login'))

        user = User_ticket.objects.filter(ticket=ticket).first()

        if not user:
            return HttpResponseRedirect(reverse('user:login'))

        if user.out_time.replace(tzinfo=None) < datetime.now():
            return HttpResponseRedirect(reverse('user:login'))

        request.user = user.user



































