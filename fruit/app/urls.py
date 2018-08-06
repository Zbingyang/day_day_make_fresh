from django.conf.urls import url
from app import views


urlpatterns = [
    # 主页
    url(r'^index/(?P<id>\d+)/', views.index, name='index'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # detail某一件商品的详情信息
    url(r'^detail/(?P<id>\d+)/', views.detail, name='detail'),
    # place_order提交订单页
    url(r'^place_order/(?P<number>\d+)', views.place_order, name='place_order'),
    # user_center_info用户中心-用户信息页，用户中心功能一，查看用户的基本信息
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # user_center_order用户中心-用户订单页，用户中心功能二，查看用户的全部订单
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # user_center_site,用户中心，用户收货地址页，用户中心功能三，查看和设置用户的收货地址
    url(r'^user_center_site/', views.user_center_site, name='user_center_site' ),
    # 查看更多商品
    url(r'^list/(?P<id>\d+)/', views.my_list, name='list'),
    # 增加购物车商品的数量
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    # 减少购物车的商品数量
    url(r'^sub_cart/', views.sub_cart, name='sub_cart'),
    # 页面一刷新，自动加载购物车里面的商品的数量
    url(r'^get_cart/', views.get_cart, name='get_cart'),
    # 算出商品的总价
    url(r'^total_price/', views.total_price, name='total_price'),
    # 在购物车内添加商品数量
    url(r'^add_count/', views.add_count, name='add_count'),
    # 在购物车内减少商品数量
    url(r'^sub_count/', views.sub_count, name='sub_count'),
    # 算出购物车的商品的总价格
    url(r'^cart_total_price/', views.cart_total_price, name='cart_total_price'),
    # 全选按钮
    url(r'^all_choice/', views.all_choice, name='all_choice'),
    # 删除单个商品
    url(r'^delete_one/', views.delete_one, name='delete_one'),
    # 获取购物车的全部商品
    url(r'^gain_cart/', views.gain_cart, name='gain_cart'),
    # 设置调用函数
    url(r'^middle/', views.middle, name='middle'),
    # 算出商品的总件数和总价格
    url(r'^total_count/', views.total_count, name='total_count'),
    # 把购物车里面商品为true的商品加入到订单模型
    url(r'^all_order/', views.all_order, name='all_order'),
    # 定义中间函数来调用ajax函数
    url(r'^show_order/', views.show_order, name='show_order'),
    # 在详情订单列表中拿出数据
    url(r'^look_order/', views.look_order, name='look_order'),
    # 提交订单，并把购物车清空，改变用户的订单的支付状态
    url(r'^pay_order/', views.pay_order, name='pay_order'),
    # xia显示登录用户的详细信息
    url(r'^show_user/',views.show_user, name='show_user'),
    # 展示用户的收货信息，并且添加新的地址
    url(r'^add_address/', views.add_address, name='add_address'),



]