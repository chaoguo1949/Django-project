from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from utils.wrappers import *
from .functions import *
from django.core.paginator import Paginator


# 商品首页
@get_total_cart_num
def index(request):

    # 读取广告信息
    ads1 = Advertise.objects.all()[:4]
    ads2 = Advertise.objects.all()[4:]

    # 获得商品所有分类
    cags = Category.objects.all()

    # 获得每一个分类的最新商品列表(显示4)，热门商品(显示3个)
    for cag in cags:
        # 获得最新商品
        new_goods = GoodsInfo.objects.get_new_goods(cag)
        # 获得最热商品
        hot_goods = GoodsInfo.objects.get_hot_goods(cag)

        cag.new = new_goods
        cag.hot = hot_goods


    return render(request, 'goods/index.html', locals())


# 商品列表页
@get_total_cart_num
def goods_list(request, cag_id, page_id):

    # 读取商品分类
    cags = Category.objects.all()
    # 获得根据价格排序　还是人气排序
    show = get(request, 'show')
    # 根据商品的分类取出对应的商品列表
    goods_list = GoodsInfo.objects.get_goods_by_cagid(cag_id, show)
    # 创建分页对象
    paginator = Paginator(goods_list, 10)
    # 获得当前页码的数据
    current_page = paginator.page(page_id)

    # 读取新品推荐
    goods_new = GoodsInfo.objects.get_new_by_all_goods()

    return render(request, 'goods/list.html', locals())


# 商品详情页
@get_total_cart_num
def goods_detail(request):

    # 查询商品信息
    goods = GoodsInfo.objects.get(pk=get(request, 'id'))
    # 获得最新商品
    goods_new = GoodsInfo.objects.get_new_by_all_goods()

    # 更新用户浏览记录
    update_user_browse_record(request)

    return render(request, 'goods/detail.html', locals())





























