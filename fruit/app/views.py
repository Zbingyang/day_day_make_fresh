from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from app.models import TypeInfo, GoodsInfo, CartInfo, OrderInfo, OrderDetailInfo, UserInfo, User_address
from utils.free import kuaidi_count


def middle(request):
    if request.method == 'GET':
        data = {
            'code':'200',
            'msg':'请求成功',
        }
        return JsonResponse(data)

def index(request,id):
    if request.method == 'GET':
        types = TypeInfo.objects.all()
        if id == 0:
            goods = GoodsInfo.objects.all()
        else:
            goods = GoodsInfo.objects.filter(gtype=id)
        data = {
            'types':types,
            'goods':goods,
            'id':id,
        }

        return render(request,'app/index.html',data)


def cart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = CartInfo.objects.filter(user_id=user.id)
            if carts:
                goods = []
                for cart in carts:
                    good = cart.goods
                    goods.append(good)
                data = {
                    'code':'200',
                    'msg':'请求成功',
                    'goods':goods,
                }

                return render(request, 'app/cart.html',data)

            else:

                return render(request, 'app/cart.html', {'data':'请先添加购物车'})

        else:
            return HttpResponseRedirect(reverse('user:login'))

    else:
        user = request.user
        if user.id:
            id = request.POST.get('id')
            number = request.POST.get('number')
            CartInfo.objects.create(user_id=user.id,
                                    goods_id=id,
                                    count=number)
            data = {
                'code':'200',
                'msg':'请求成功'
            }
            return JsonResponse(data)
        else:
            data = {
                'code':'1001',
                'msg':'请求成功'
            }
        return JsonResponse(data)

def cart_total_price(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            total_list = []
            carts = CartInfo.objects.filter(user_id=user.id)
            for cart in carts:
                total_price = cart.count * cart.goods.gprice
                id = cart.goods.id
                total = {
                    'id':id,
                    'total_price':total_price,
                }
                total_list.append(total)
            data = {
                'total_list':total_list,
                'code':'200',
                'msg':'请求成功'
            }
            return JsonResponse(data)

        else:
            data = {
                'code':'1001',
                'msg':'请求失败'
            }
            return JsonResponse(data)


def sub_count(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            id = request.POST.get('id')
            cart = CartInfo.objects.filter(user_id=user.id,goods_id=id).first()
            if cart.count == 1:
                cart.delete()
                number = 1
                data = {
                    'code':'200',
                    'msg':'请求成功',
                    'number':number,
                }
                return JsonResponse(data)
            else:
                cart.count -= 1
                cart.save()
                number = cart.count
                data = {
                    'code':'200',
                    'msg':'请求成功',
                    'number':number,
                }
                return JsonResponse(data)

        else:
            data = {
                'code':'1001',
                'msg':'请求失败'
            }
            return JsonResponse(data)

def add_count(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            id = request.POST.get('id')
            cart = CartInfo.objects.filter(user_id=user.id, goods_id=id).first()
            cart.count += 1
            number = cart.count
            cart.save()
            data = {
                'code':'200',
                'number':number,
                'msg':'请求成功'
            }
            return JsonResponse(data)
        else:
            data = {
                'code': '1001',
                'msg': '请求失败'
            }
            return JsonResponse(data)

def add_cart(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['msg'] = '请求失败'
        data['code'] = '1001'
        if user.id:
            id = request.POST.get('id')
            number = request.POST.get('number')
            good = GoodsInfo.objects.get(id=id)
            cart = CartInfo.objects.filter(user=user.id,goods=good.id).first()
            if cart:
                cart.count += 1
                data['msg'] = '请求成功'
                data['code'] = '200'
                data['number'] = cart.count
                cart.save()
                return JsonResponse(data)

            else:
                CartInfo.objects.create(user_id=user.id,
                                    goods_id=good.id,
                                    count=number)
                data['msg'] = '请求成功'
                data['code'] = '200',
                data['number'] = 2
                return JsonResponse(data)
        return JsonResponse(data)


# 获取购物车的全部商品
def gain_cart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = CartInfo.objects.filter(user_id=user.id)
            goods_list = []
            for cart in carts:
                good = cart.goods
                goods = {
                    'good':[{'good_gpic':str(good.gpic),
                             'good_gprice':good.gprice,
                             'good_gtitle':good.gtitle,
                             'good_gunit':good.gunit,
                             'good_id':good.id,
                             'number':cart.count}],
                }
                goods_list.append(goods)
            data = {
                'code':'200',
                'msg':'请求成功',
                'goods_list':goods_list,
            }
            return JsonResponse(data)


    else:
        pass


def sub_cart(request):
    user = request.user
    data = {}
    data['code'] = '1001'
    data['msg'] = '请求失败'
    if user.id:
        id = request.POST.get('id')
        cart = CartInfo.objects.filter(goods_id=id,user_id=user.id).first()
        if cart:
            if cart.count == 1:
                cart.delete()
                data['number'] = 1
                data['code'] = '200'
                data['msg'] = '请求成功'
                return JsonResponse(data)

            else:
                cart.count -= 1
                data['number'] = cart.count
                data['code'] = '200'
                data['msg'] = '请求成功'
                cart.save()
                return JsonResponse(data)

        else:
            data['number'] = 1
            data['msg'] = '您还没有加入购物车'
            return JsonResponse(data)

    return JsonResponse(data)


def get_cart(request):
    if request.method == 'GET':
        data = {}
        user = request.user
        if user.id:
            carts = CartInfo.objects.filter(user_id=user.id)
            message = []
            for cart in carts:
                id = cart.goods_id
                data = {
                    'number':cart.count,
                    'id':id,
                    'code':'200',
                }
                message.append(data)
            goods = {'message':message}

            return JsonResponse(goods)
        else:
            data['code'] = '1001'
            data['msg'] = '请求失败'
            return JsonResponse(data)


# 算出总价格
def total_price(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            id = request.POST.get('id')
            cart = CartInfo.objects.filter(user_id=user.id,goods_id=id,is_select=True).first()
            if cart:
                total_price = cart.count * cart.goods.gprice
                total_price = round(total_price, 2)
                data = {
                    'total_price':total_price
                }
                return JsonResponse(data)

            else:
                good = GoodsInfo.objects.get(id=id)
                total_price = good.gprice
                total_price = round(total_price, 2)
                data = {
                    'code':'200',
                    'total_price':total_price
                }
                return JsonResponse(data)
        else:
            data = {
                'code':'1001',
                'msg':'请求失败'
            }
            return JsonResponse(data)


def all_choice(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            checked = request.POST.get('checked')
            carts = CartInfo.objects.all()
            if checked:
                for cart in carts:
                    cart.is_select = False
                    is_checked =  cart.is_select
                    cart.save()
                data = {
                    'code':'200',
                    'msg':'请求成功',
                    'is_checked':is_checked,
                }
                return JsonResponse(data)

            else:
                for cart in carts:
                    cart.is_select = True
                    is_checked = cart.is_select
                    cart.save()
                data = {
                    'code': '200',
                    'msg': '请求成功',
                    'is_checked':is_checked,
                }
                return JsonResponse(data)

        else:
            data = {
                'code':'1001',
                'msg':'请求失败'
            }
        return JsonResponse(data)


def delete_one(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            id = request.POST.get('id')
            cart = CartInfo.objects.filter(goods_id=id,user_id=user.id).first()
            cart.delete()
            data = {
                'code':'200',
                'msg':'请求成功',
            }
            return JsonResponse(data)
        else:
            data = {
                'code':'200',
                'msg':'请求失败'
            }
        return JsonResponse(data)


# 计算商品的总价和 总数
def total_count(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = CartInfo.objects.filter(user_id=user.id)
            price_list = []
            all_price = 0
            if carts:
                for cart in carts:
                    count = cart.count
                    price = cart.goods.gprice
                    all_price += count * price
                count = len(carts)

                data = {
                    'code':'200',
                    'msg':'请求成功',
                    'all_price':all_price,
                    'count':count,
                }
                return JsonResponse(data)
            else:
                data ={
                    'code':200,
                    ' msg':'1001',
                    'count':0,
                    'all_price':0,
                }

            return JsonResponse(data)


# 把购物车的属性为true的商品加入到订单表中
def all_order(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            carts = CartInfo.objects.filter(user_id=user.id,is_select=True)
            if carts:
                total = 0
                for cart in carts:
                    end_price = cart.goods.gprice * cart.count
                    total += end_price
                number = kuaidi_count()
                order = OrderInfo.objects.create(
                                        order_id=number,
                                        user_id=user.id,
                                         ototal=total,
                                         oaddress=user.uaddress,
                                         )
                for cart in carts:
                    goods_price = cart.count * cart.goods.gprice
                    OrderDetailInfo.objects.create(goods_id=cart.goods.id,
                                                   order_id= order.order_id,
                                                   price=goods_price,
                                                   count= cart.count
                                                   )
                data = {
                    'order': number,
                    'code': '200',
                    'msg': '请求成功'
                }
                return JsonResponse(data)
            else:
                data = {
                    'code': '1001',
                    'msg': '请求失败'
                }

                return JsonResponse(data)

        else:
            data = {
                'code': '200',
                'msg': '请求失败'
            }
            return JsonResponse(data)


# 定义中间函数
def show_order(request):
    if request.method == 'GET':
        data = {
            'code':'200',
            'msg':'请求成功'
        }
        return JsonResponse(data)
# 单个商品的详细信息
def detail(request, id):
    if request.method == 'GET':
        good = GoodsInfo.objects.get(id=id)
        data = {
            'good': good
        }
        return render(request, 'app/detail.html', data)


# 订单列表
def place_order(request, number):
    if request.method == 'GET':
        data = {'number': number}
        return render(request, 'app/place_order.html',data)


def look_order(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            order = request.POST.get('order')
            order_details = OrderDetailInfo.objects.filter(order_id=order)
            order_goods = []
            end_price = 0
            for order_detail in order_details:
                end_price += order_detail.price
                goods = {
                    'good': [{'price': order_detail.price,
                              'count': order_detail.count,
                              'img': str(order_detail.goods.gpic),
                              'gunit': order_detail.goods.gunit,
                              'good_id': order_detail.goods.id,
                              'good_title' : order_detail.goods.gtitle ,
                              'good_price': order_detail.goods.gprice,
                              }],
                        }
                order_goods.append(goods)
            data = {
                'code': '200',
                'msg': '请求成功',
                'order_goods': order_goods,
                'end_price':end_price,
            }
            return JsonResponse(data)
        else:
            data = {
                'code':'1001',
                'msg':'请求失败',
            }
            return JsonResponse(data)


# 提交订单，并把购物车清空，改变用户的订单的支付状态,传入订单号，找出对应的订单详情表的的商品，再用详情表的商品找出对应的购物车里面的商品。
def pay_order(request):
     if request.method == 'POST':
         user = request.user
         if user.id:
             id = request.POST.get('order')
             order = OrderInfo.objects.get(order_id=id)
             order.oIsPay = True
             order.save()
             order_details = OrderDetailInfo.objects.filter(order_id=id)
             for order_detail in order_details:
                 order_detail.goods.cartinfo_set.all().delete()

             data = {
                 'code':'200',
                 'msg':'请求成功'
             }
             return JsonResponse(data)
         else:
             data = {
                 'code':'1001',
                 'msg':'请求失败'
             }
             return JsonResponse(data)


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'app/user_center_info.html')


# 查询用户的已经支付的订单情况
def user_center_order(request):
    user = request.user
    if user.id:
        # 查询数据
        orders = OrderInfo.objects.filter(user_id=user.id)
        # 生成分页实列
        paginate = Paginator(orders,2)
        # 获取当前页码
        pageIndex = request.GET.get('pageIndex',1)
        # 获取当前页面的数据
        pagedata = paginate.page(pageIndex)
        data = {'orders':pagedata,
             }
        return render(request, 'app/user_center_order.html',data)

# 查询用户的没有支付的订单情况
# def select_oIspay_order(request):
#     user = request.user
#     if user.id:
#         orders = OrderInfo.objects.filter(user_id=user.id,oIsPay=True)
#         orders_list = []
#         goods_list = []
#         for order in orders:
#             order_details = OrderDetailInfo.objects.filter(order_id=order.order_id)
#             for order_detail in order_details:
#                 goods = {'good':[{
#                     'order':order.oIsPay,
#                     'good_gtitle':order_detail.goods.gtitle,
#                     'good_gpic':str(order_detail.goods.gpic),
#                     'good_price':order_detail.goods.gprice,
#                     'good_gunit':order_detail.goods.gunit,
#                     'order_id':order.order_id,
#                 }]}
#
#                 goods_list.append(goods)
#             orders = {'orders': [{
#                 'order_id': order.order_id,
#                 'order_pay': order.oIsPay,
#                 'goods_list':goods_list,
#             }]}
#             orders_list.append(orders)
#
#         data = {
#             'code':'200',
#             'msg':'请求成功',
#             'orders':orders,
#         }
#         return JsonResponse(data)
#
#     data = {
#         'code':'1001',
#         'msg':'请求失败',
#     }
#     return JsonResponse(data)
#


# 显示用户的信息，用户的详情页面
def show_user(request):
    user = request.user
    if user.id:
        user = UserInfo.objects.get(id=user.id)
        user = {
            'uname':user.uname,
            'ushow':user.ushow,
            'uaddress':user.uaddress,
            'uphone':user.uphone,
        }
        data = {
            'code':'200',
            'msg':'请求成功',
            'user':user,
        }
        return JsonResponse(data)
    data = {
        'code':'1001',
        'msg':'请求失败',
    }
    return JsonResponse(data)


def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'app/user_center_site.html')


# 用户的订单的收货地址
def add_address(request):
    user = request.user
    if user.id:
        consignee = request.POST.get('consignee')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        User_address.objects.create(user_id=user.id,
                                    phone=phone,
                                    address=address,
                                    email=email,
                                    consignee=consignee)
        data = {
            'code':'200',
            'msg':'请求成功'
        }
        return JsonResponse(data)

    data = {
        'code':'1001',
        'msg':'请求失败',
    }
    return JsonResponse(data)




def my_list(request, id):
    if request.method == 'GET':
        goods = GoodsInfo.objects.filter(gtype=id)
        types = TypeInfo.objects.all()
        data = {
            'goods':goods,
            'types':types,
        }
        return  render(request, 'app/list.html', data)