from django.shortcuts import render
from django.http import HttpResponse
from utils.wrappers import *
from carts.models import *
from users.models import *
from django.http import JsonResponse
from .models import *
import time
import random
from django.db import transaction


# 订单首页
def index(request):

    goods_ids = post_list(request, 'goods_id')

    # 将商品ID拼接成字符串
    goods_string = ','.join(goods_ids)

    # 查询商品
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'), cart_goods_id__in=goods_ids)

    total_nums = 0
    total_money = 0

    for cart in carts:
        # 计算单品总价
        cart.total = cart.cart_amount * cart.cart_goods.goods_price
        # 累计商品总数量
        total_nums += cart.cart_amount
        # 累计商品总价格
        total_money += cart.total


    carts.total_nums = total_nums
    carts.total_money = total_money

    # 获取用户信息
    user = User.objects.get(id=get_session(request, 'uid'))


    return render(request, 'order/place_order.html', locals())


# 处理订单提交
@transaction.atomic
def order_handle(request):


    # 1. 获得商品ID列表 付款方式
    goods_ids = post(request, 'ids').split(',')
    goods_pay = post(request, 'pay')
    user_id = get_session(request, 'uid')
    # 2. 获得商品列表
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'),
                        cart_goods_id__in=goods_ids)


    # 获取用户信息
    user = User.objects.get(id=user_id)

    # 创建一个存档(保存点)
    save_point = transaction.savepoint()

    try:
        # 创建订单基础信息
        order = Order()
        order.order_addr = user.user_addr
        order.order_recv = user.user_recv
        order.order_pay = goods_pay
        order.order_user = user
        # 订单编号
        order.order_number = str(user_id) + str(int(time.time())) + str(random.randint(1000, 9999))
        order.save()

        for cart in carts:

            # 创建订单商品信息
            detail = GoodsDetail()
            detail.detail_amount = cart.cart_amount
            detail.detail_goodsid = cart.cart_goods_id
            detail.detail_img = cart.cart_goods.goods_image
            detail.detail_price = cart.cart_goods.goods_price
            detail.detail_name = cart.cart_goods.goods_name
            detail.detail_unit = cart.cart_goods.goods_unit
            detail.detail_goods = order
            detail.save()

        # 删除购物车中商品
        carts.delete()

        # 提交事务
        transaction.savepoint_commit(save_point)
    except:

        # 滚回到保存点
        transaction.savepoint_rollback(save_point)
        return JsonResponse({'ret': 0})

    return JsonResponse({'ret': 1})


















