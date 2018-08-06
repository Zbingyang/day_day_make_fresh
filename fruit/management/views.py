from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
# from app.models import TypeInfo,GoodsInfo
from django.core.paginator import Paginator

from app.models import GoodsInfo, TypeInfo


def login(request):
    if request.method == 'GET':
        return render(request, 'management/login.html')

    else:
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        if num1 == num2:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('management:index'))

            else:
                return HttpResponseRedirect(reverse('management:login'))


def index(request):
    return render(request, 'management/index.html')


def product_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num',1)
        goods = GoodsInfo.objects.all()
        paginator = Paginator(goods, 3)
        page = paginator.page(int(page_num))
        data = {'goods':page}
        return render(request, 'management/product_list.html',data)


def product_detail(request):
    if request.method == 'GET':
        product_details = TypeInfo.objects.all()
        data = {'product_details':product_details}
        return render(request, 'management/product_detail.html',data)

    else:
        goods_name = request.POST.get('shop_name')
        goods_num = request.POST.get('shop_num')
        type = request.POST.get('goods_type')
        gprice = request.POST.get('price')
        goods_type = TypeInfo.objects.get(id=type)
        goods_file = request.FILES.get('img')
        GoodsInfo.objects.create(gtitle=goods_name,
                                 gpic=goods_file,
                                 gjianjie=goods_num,
                                 gtype=goods_type,
                                 gprice=gprice)
        return HttpResponseRedirect(reverse('management:product_list'))





def recycle_bin(request):
    if request.method == 'GET':
        return render(request, 'management/recycle_bin.html')


def order_list(request):
    if request.method == 'GET':
        return render(request, 'management/order_list.html')


def order_detail(request):
    if request.method == 'GET':
        return render(request, 'management/order_detail.html')


def user_list(request):
    if request.method == 'GET':
        return render(request, 'management/user_list.html')


def user_detail(request):
    if request.method == 'GET':
        return render(request, 'management/user_detail.html')


def user_rank(request):
    if request.method == 'GET':
        return render(request, 'management/user_rank.html')


def adjust_funding(request):
    if request.method == 'GET':
        return render(request, 'management/adjust_funding.html')


def setting(request):
    if request.method == 'GET':
        return render(request, 'management/setting.html')


def express_list(request):
    if request.method == 'GET':
        return render(request, 'management/express_list.html')


def pay_list(request):
    if request.method == 'GET':
        return render(request, 'management/pay_list.html')


def discharge_statistic(request):
    if request.method == 'GET':
        return render(request, 'management/discharge_statistic.html')


def sales_volume(request):
    if request.method == 'GET':
        return render(request, 'management/sales_volume.html')


def logout(request):
    if request.method == 'GET':
        request.COOKIES.clear()
        return HttpResponseRedirect(reverse('management:login'))
