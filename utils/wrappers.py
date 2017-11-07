import hashlib
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


# post
def post(request, key):
    return request.POST.get(key, '').strip()


# post list
def post_list(request, key):
    return request.POST.getlist(key)


# get
def get(request, key):
    return request.GET.get(key, '').strip()


# 设置cookie
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获得cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获得session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session
def del_session(request):
    request.session.flush()


# 用户密码加密
def password_encryption(password, salt=''):

    sha = hashlib.sha256()
    new_password = '$%^$%^@$%@' + password + salt + '*(&^%$#DSFGDRS'
    sha.update(new_password.encode('utf-8'))

    return sha.hexdigest()


# 添加信息
def add_message(request, key, value):
    messages.add_message(request, messages.INFO, key + ":" + value)


# 获得信息
def get_messages(request):

    # 取出所有错误信息
    mess = messages.get_messages(request)
    # 保存错误信息到字典中
    info = dict()
    for message in mess:
        content = str(message).split(':')
        info[content[0]] = content[1]

    return info


# 判断用户是否登陆
def check_user_login(request):
    return get_session(request, 'username')


# 检测用户权限
def check_permission(view_func):

    def wrapper(request, *args, **kwargs):
        # 判断用户是否登陆
        if check_user_login(request):
            # 调用视图函数
            return view_func(request, *args, **kwargs)

        # 如果用户登录失败,跳转到登陆页面
        else:
            return redirect(reverse('users:login'))


    return wrapper







