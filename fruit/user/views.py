from datetime import datetime,timedelta

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app.models import UserInfo,User_ticket
from django.contrib.auth.hashers import make_password,check_password
from utils.free import ran


def register(request):
    if request.method == 'GET':
        return render(request,'app/register.html')

    if request.method == 'POST':
        uname = request.POST.get('user_name')
        upwd = request.POST.get('pwd')
        uemail = request.POST.get('email')
        UserInfo.objects.create(uname=uname,
                                upwd=make_password(upwd),
                                uemail=uemail)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request,'app/login.html')

    if request.method == 'POST':
        uname = request.POST.get('username')
        user = UserInfo.objects.get(uname=uname)
        if user.id:
            password = request.POST.get('pwd')
            if check_password(password,user.upwd):
                free = ran()
                out_time = datetime.now() + timedelta(days=10)
                res = HttpResponseRedirect(reverse('app:index', kwargs={'id':0}))
                res.set_cookie('ticket',free,expires=out_time)
                User_ticket.objects.create(ticket=free,out_time=out_time,user_id=user.id)
                return res

            else:
                return HttpResponseRedirect(reverse('user:login'))


        else:
            return HttpResponseRedirect(reverse('user；login'))


def logout(request):
    pass

