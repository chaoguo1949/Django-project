from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    # 添加商品到购物车
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
    # 修改商品数量
    url(r'^edit_goods/$', views.edit_goods_num, name='edit_goods_num'),
    # 删除商品
    url(r'^remove_goods/$', views.remove_goods, name='remove_goods'),
]