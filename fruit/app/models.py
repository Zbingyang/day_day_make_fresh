#coding=utf-8

from django.db import models

# 构建用户模型
from django.db.models import PROTECT


class UserInfo(models.Model):
    # u'***'修改的是后台展示信息的名字字段
    uname = models.CharField(u'用户名', max_length=20)
    # 密码采用暗文，sha1加密转换为40字节
    upwd = models.CharField(u'密码', max_length=500)
    uemail = models.CharField(u'电子邮箱', max_length=30)
    ushow = models.CharField(u'收件人名字', max_length=20, default='')
    uaddress = models.CharField(u'收件地址', max_length=100, default='')
    uyoubian = models.CharField(u'收件邮编', max_length=6, default='')
    uphone = models.CharField(u'收件人电话', max_length=11, default='')

    # default,blank是python层面的约束,不影响数据库表结构

    # 用户对象名字返回，后台订单管理现实
    def __str__(self):
        return self.uname

    # 修改后台管理界面显示
    class Meta:
        verbose_name_plural = '用户管理'
        verbose_name = '用户'


#用户关联的地址
class User_address(models.Model):
    phone = models.CharField(max_length=11,null=False)
    consignee = models.CharField(max_length=200,null=False)
    address = models.CharField(max_length=200,null=False)
    user = models.ForeignKey(UserInfo,on_delete=PROTECT)
    email = models.CharField(max_length=200,null=False)


    class Meta():
        db_table = 'address'












class User_ticket(models.Model):
    ticket = models.CharField(max_length=500,default='')
    create_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(default=0)
    user = models.ForeignKey(UserInfo,on_delete=PROTECT)

    class Meta():
        db_table = 'user_ticket'


# 订单表模型
class OrderInfo(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserInfo,on_delete=PROTECT)
    odate = models.DateTimeField(u'购买日期',auto_now=True)
    # 付款属性
    oIsPay = models.BooleanField(u'是否付款',default=False)
    # 总价
    ototal = models.DecimalField(u'总价',max_digits=6, decimal_places=2,null=False)
    oaddress = models.CharField(u'收货地址',max_length=150,null=False)


    def __str__(self):
        if self.oIsPay==True:
            return self.oaddress
        else :
            return '未付款'

    # 修改后台显示名字
    class Meta:
        verbose_name_plural='订单管理'


# 商品类型模型
class TypeInfo(models.Model):
    # u'***'是在后台注册时替换属性名字
    ttitle=models.CharField(u'种类',max_length=20)
    type_img = models.CharField(max_length=500,default='')
    isDelete=models.BooleanField(default=False)
    # 商品类型对象返回名字
    def __str__(self):
        return self.ttitle

    class Meta:
        verbose_name_plural = '水果类型修改'
        verbose_name = '学科'


# 商品模型
class GoodsInfo(models.Model):
    gtitle=models.CharField(u'名字',max_length=20)
    gpic=models.ImageField(u'图片',upload_to='upload')
    gprice=models.DecimalField(u'价钱',max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(u'单位',max_length=20,default='500g')
    gclick=models.IntegerField(u'点击',default=0)
    gjianjie=models.CharField(max_length=200)
    gkucun=models.IntegerField(u'库存',default=100)
    gcontent=models.CharField(u'描述',default='很好',max_length=200)
    # 引用外键
    gtype = models.ForeignKey(TypeInfo,on_delete=PROTECT)
    # 商品对象名字返回

    def __str__(self):
        return self.gtitle

    class Meta:
        verbose_name_plural = '水果'
        verbose_name = '水果'


# 购物车模型
class CartInfo(models.Model):
    # 外键用户
    user=models.ForeignKey(UserInfo,on_delete=PROTECT)
    # 外键商品
    goods=models.ForeignKey(GoodsInfo,on_delete=PROTECT)
    # 购买的数量
    count=models.IntegerField()
    # 选中与没有选中
    is_select = models.BooleanField(default=True)


# 订单详表
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo,on_delete=PROTECT)
    order = models.ForeignKey(OrderInfo,on_delete=PROTECT)
    # 总价
    price = models.DecimalField(u'价钱',max_digits=5, decimal_places=2)
    # 数量
    count = models.IntegerField(u'数量')
    # 统计销量是否统计进去
    isTrue=models.BooleanField(default=False)

    # 修改后台显示名字
    class Meta:
        verbose_name_plural = '发货管理'


# 销量统计
class sales(models.Model):
    # 水果名称
    goods = models.ForeignKey(GoodsInfo, on_delete=PROTECT)
    # 销量
    count = models.IntegerField(u'销量')
    # 销售额
    totalprice = models.DecimalField(u'销售额', max_digits=5, decimal_places=2)

    # 修改后台显示名字

    class Meta:
        verbose_name_plural = '销量查看'

    def __str__(self):
        return self.goods.gtitle








