from django.conf.urls import url
from management import views

urlpatterns = [

    url(r'^login/', views.login, name='login'),

    url(r'^index/', views.index, name='index'),

    url(r'^product_list/', views.product_list, name='product_list'),

    url('^product_detail/', views.product_detail, name='product_detail'),

    url(r'^recycle_bin/', views.recycle_bin, name='recycle_bin'),

    url(r'^order_list/', views.order_list, name='order_list'),

    url(r'^order_detail/', views.order_detail, name='order_detail'),

    url(r'^user_list/', views.user_list, name='user_list'),

    url(r'^user_detail/', views.user_detail, name='user_detail'),

    url(r'^user_rank/', views.user_rank, name='user_rank'),

    url(r'^adjust_funding/', views.adjust_funding, name='adjust_funding'),

    url(r'^setting/', views.setting, name='setting'),

    url(r'^express_list/', views.express_list, name='express_list'),

    url(r'^pay_list/', views.pay_list, name='pay_list'),

    url(r'^discharge_statistic/', views.discharge_statistic, name='discharge_statistic'),

    url(r'^logout/', views.logout, name='logout'),

    url(r'^sales_volume/', views.sales_volume, name='sales_volume'),

]











