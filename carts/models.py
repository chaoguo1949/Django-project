from django.db import models
from db.AbstractModel import *


# 购物车管理器类
class CartManager(models.Manager):
    pass


# 购物车模型
class Cart(AbstractModel):

    # 购买商品
    cart_goods = models.ForeignKey('goods.GoodsInfo')
    # 购买数量
    cart_amount = models.IntegerField()
    # 所属用户
    cart_user = models.ForeignKey('users.User')

    objects = CartManager()

