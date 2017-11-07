from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 配置视图
    url(r'^detail/$', views.goods_detail, name='detail'),
    url(r'^list/(\d+)/(\d+)/$', views.goods_list, name='list'),
]