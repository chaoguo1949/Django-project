from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


# 分类模型
class Category(AbstractModel):

    # 产品分类名称
    cag_name = models.CharField(max_length=30)


# 商品信息管理类
class GoodsInfoManager(models.Manager):


    # 获得最新添加的商品(4个)
    def get_new_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    # 热门商品(3个)
    def get_hot_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('-goods_visits')[:3]

    # 获得所有商品中最新的两个商品
    def get_new_by_all_goods(self):
        return self.all().order_by('-id')[:2]

    # 根据商品分类的id获取商品列表
    def get_goods_by_cagid(self, cag_id, show):

        if show == 'price':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_price')

        if show == 'hot':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_visits')

        return self.filter(goods_cag_id=cag_id)



# 商品信息
class GoodsInfo(AbstractModel):

    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品价格
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品的图片
    goods_image = models.ImageField()
    # 商品简述
    goods_short = models.CharField(max_length=100)
    # 商品详情
    goods_desc = HTMLField()
    # 商品上架
    goods_status = models.BooleanField(default=True)
    # 商品单位
    goods_unit = models.CharField(max_length=20)
    # 商品访问量
    goods_visits = models.IntegerField(default=0)
    # 商品销量
    goods_sales = models.IntegerField(default=0)
    # 商品分类
    goods_cag = models.ForeignKey(Category)


    objects = GoodsInfoManager()


# 广告模型
class Advertise(AbstractModel):

    # 广告名字
    ad_name = models.CharField(max_length=30)
    # 广告图片
    ad_image = models.ImageField(upload_to='ad')
    # 广告链接
    ad_link = models.CharField(max_length=100)

















