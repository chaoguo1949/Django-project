from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .functions import *
from .models import *
from django.http import JsonResponse
from order.models import *
from django.core.paginator import Paginator


# 用户中心首页
@check_permission
def index(request):
    user = User.objects.user_by_name(get_session(request, 'username'))
    # records = RecordBrowse.objects.filter(browse_user_id=get_session(request, 'uid')).order_by('-update_time')
    return render(request, 'users/user_center_info.html', locals())


# 用户中心订单页面
@check_permission
def user_order(request):

    orders = Order.objects.filter(order_user_id=get_session(request, 'uid'))

    # 分页显示
    paginator = Paginator(orders, 2)
    # 获取当前分页
    current_page = get(request, 'page')
    if not current_page:
        current_page = 1

    orders = paginator.page(current_page)

    for order in orders:
        order.total = 0
        for goods in order.goodsdetail_set.all():
            order.total += goods.detail_amount * goods.detail_price

    return render(request, 'users/user_center_order.html', locals())


# 用户中心地址编辑页面
@check_permission
def user_address(request):
    user = User.objects.user_by_name(get_session(request, 'username'))
    return render(request, 'users/user_center_site.html', locals())


# 用户登陆页面
def login(request):
    return render(request, 'users/login.html', locals())


# 注册页面
def register(request):

    # 取出错误信息
    mess = get_messages(request)

    return render(request, 'users/register.html', locals())


# 处理注册
def register_handle(request):

    # 检测注册参数是否合法
    if check_register_params(request):
        # 用户信息入库
        User.objects.user_register_save(request)
        # 跳转到登陆页面
        return redirect(reverse('users:login'))

    # 参数不合法跳转回注册页面
    else:
        return redirect(reverse('users:register'))


# 检测用户名是否存在
def check_username(request):

    # 如果用户存在
    if user_is_exist(request):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})


# 处理登录
def login_handle(request):

    # 对用户名和密码做简单的校验
    if check_login_params(request):
        # 1. 记录用户状态(写session)
        keep_user_online(request)

        response = redirect(get_redirect_url(request))
        # 2. 是否需要记录用户名(写cookie)
        remember_username(request, response)

        return response

    # 登陆失败跳转回登陆页面
    else:
        return redirect(reverse('users:login'))


# 注销处理
def logout(request):

    # 先保存上一页面
    url = get_redirect_url(request)
    # 1. 清除session
    del_session(request)
    # 2. 跳转上一页面
    return redirect(url)


# 处理修改收人信息
def address_edit(request):

    # 如果提交参数没有问题
    if check_address_edit_params(request):
        # 更新用户地址信息
        User.objects.user_address_update(request)

    # 跳转到用户中心地址页面
    return redirect(reverse('users:address'))


















