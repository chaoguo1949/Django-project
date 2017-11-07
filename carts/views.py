from django.shortcuts import render
from django.http import HttpResponse
from utils.wrappers import *
from .models import *
from django.http import JsonResponse


@check_permission
def index(request):


    # 取出购物车数据
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
    # 记录总数量
    total = 0
    # 记录总价格
    money = 0
    # 遍历购物车统计
    for cart in carts:
        # 计算单品总价
        cart.single_total = cart.cart_amount * cart.cart_goods.goods_price
        # 累加商品总数量
        total += cart.cart_amount
        # 累加商品总价格
        money += cart.single_total

    carts.total = total
    carts.money = money

    return render(request, 'carts/cart.html', locals())


# 商品添加到购物车
def add_goods(request):

    # 1. 获取用户ID、商品ID、商品数量
    goods_id = get(request, 'goods_id')
    user_id = get_session(request, 'uid')
    goods_num = get(request, 'goods_num')

    # 2. 先判断该商品是否在购物车中存在

    # 2.1 如果存在，则只更新商品的数量
    try:
        cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        cart.cart_amount = cart.cart_amount + int(goods_num)
        cart.save()

    # 2.2 如果不存在，新增一条购物车商品数据
    except Cart.DoesNotExist:
        c = Cart()
        c.cart_goods_id = goods_id
        c.cart_user_id = user_id
        c.cart_amount = goods_num
        c.save()

    # 将当前购物车商品数量总和返回
    # 通过聚合计算商品总数量
    # Cart.objects.filter(cart_user_id=user_id).aggregate(models.Sum('cart_amount'))
    carts = Cart.objects.filter(cart_user_id=user_id)
    total = 0
    for cart in carts:
        total += cart.cart_amount

    return JsonResponse({'total': total})


# 修改商品数量
def edit_goods_num(request):

    # 获得商品ID
    goods_id = get(request, 'id')
    # 获得商品数量
    goods_num = get(request, 'num')
    # 更新当前用户购物车商品数量信息
    try:
        # 更新商品数量
        cart = Cart.objects.get(cart_user_id=get_session(request, 'uid'), cart_goods_id=goods_id)
        cart.cart_amount = goods_num
        cart.save()

    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})

    return JsonResponse({'ret': 1})


# 删除购物车商品
def remove_goods(request):

    # 获得删除的商品ID
    goods_id = get(request, 'id')
    # 查询数据
    try:
        cart = Cart.objects.get(cart_user_id=get_session(request, 'uid'), cart_goods_id=goods_id)
        cart.delete()

    except:
        pass

    return JsonResponse({'ret': 1})










