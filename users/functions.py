from utils.wrappers import *
from .models import *
import re
import hashlib
from django.contrib import messages
from django.core.urlresolvers import reverse


# 用户注册信息校验
def check_register_params(request):

    # 获得注册参数
    user_name = post(request, 'user_name')
    user_mail = post(request, 'user_mail')
    user_pass1 = post(request, 'user_pass1')
    user_pass2 = post(request, 'user_pass2')

    flag = True

    # 判断用户长度
    if not (5 <= len(user_name) <= 20):
        flag = False
        add_message(request, 'user_name', '用户名长度应该在5-20之间!')

    # 判断密码长度
    if not (8 <= len(user_pass1) <= 20):
        flag = False
        add_message(request, 'user_pass', '密码长度应该在8-20之间!')

    # 判断密码是否相等
    if user_pass1 != user_pass2:
        flag = False
        add_message(request, 'user_pass', '两次输入的密码不一致!')

    # 判断邮箱是否合法
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_mail):
        flag = False
        add_message(request, 'user_mail', '邮箱格式不正确!')

    # 判断用户名是否存在
    if User.objects.user_by_name(user_name):
        flag = False
        add_message(request, 'user_name', '用户名存在!')

    return flag


# 检测用户名是否存在
def user_is_exist(request):

    # 获得请求参数
    username = get(request, 'username')
    # 查询用户数据
    return User.objects.user_by_name(username)


# 检测登陆参数是否合法
def check_login_params(request):

    # 获取表单数据
    user_name = post(request, 'user_name')
    user_pass = post(request, 'user_pass')

    #　对数据做校验
    if not (5 <= len(user_name) <= 20):
        return False

    if not (8 <= len(user_pass) <= 20):
        return False


    # 检测用户是否存在
    user = User.objects.user_by_name(user_name)
    if not user:
        return False
    else:
        if user.user_pass == password_encryption(user_pass):
            return True
        else:
            return False


# 记录用户登录状态
def keep_user_online(request):
    user = User.objects.user_by_name(post(request, 'user_name'))
    set_session(request, 'username', user.user_name)
    set_session(request, 'uid', user.id)


# 记住用户名
def remember_username(request, response):

    # 是否记录用户名参数
    username_member = post(request, 'user_memb')
    if username_member:
        # 将用户名写入cookie
        set_cookie(response, 'username', post(request, 'user_name'))


# 获得跳转url
def get_redirect_url(request):

    # 先获得上一次url
    url = get_cookie(request, 'pre_url')
    if not url:
        url = reverse('users:index')

    return url


# 检查修改地址的参数
def check_address_edit_params(request):

    # 获取表单数据
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    user_tele = post(request, 'user_tele')

    if len(user_recv) == 0:
        return False

    if len(user_addr) == 0:
        return False

    if len(user_code) != 6:
        return False

    if len(user_tele) != 11:
        return False

    return True



































































