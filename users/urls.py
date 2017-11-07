from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^address/$', views.user_address, name='address'),
    url(r'^order/$', views.user_order, name='order'),
    # 处理用户注册
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    # 检测用户名是否存在
    url(r'^check_username/$', views.check_username, name='check_username'),
    # 处理登录
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    # 用户注销登录
    url(r'^logout/$', views.logout, name='logout'),
    # 处理用户地址修改
    url(r'^address_edit/$', views.address_edit, name='address_edit')
]