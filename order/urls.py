from django.conf.urls import url
from . import views


urlpatterns = [
    # 配置首页视图
    url(r'^index/$', views.index, name='index'),
    # 处理订单提交
    url(r'^order_handle/$', views.order_handle, name='order_handle'),
]