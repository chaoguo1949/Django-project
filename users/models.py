from django.db import models
from db.AbstractModel import *
from utils.wrappers import *


# 用户管理器类
class UserManager(models.Manager):

    # 根据用户名获得用户数据
    def user_by_name(self, username):
        try:
            return self.get(user_name=username)
        except User.DoesNotExist:
            return None


    # 用户注册数据保存
    def user_register_save(self, request):

        user = self.model()
        user.user_name = post(request, 'user_name')
        user.user_pass = password_encryption(post(request, 'user_pass1'))
        user.user_mail = post(request, 'user_mail')

        user.save()


    # 修改用户地址
    def user_address_update(self, request):
        # 获得用户数据
        user = self.user_by_name(get_session(request, 'username'))
        # 更新用户地址信息
        user.user_tele = post(request, 'user_tele')
        user.user_code = post(request, 'user_code')
        user.user_addr = post(request, 'user_addr')
        user.user_recv = post(request, 'user_recv')
        # 更新数据
        user.save()


# 用户模型类
class User(AbstractModel):

    # 用户名
    user_name = models.CharField(max_length=20)
    # 用户密码
    user_pass = models.CharField(max_length=100)
    # 用户邮箱
    user_mail = models.CharField(max_length=50)
    # 用户地址
    user_addr = models.CharField(max_length=50)
    # 用户手机
    user_tele = models.CharField(max_length=11)
    # 邮政编码
    user_code = models.CharField(max_length=10)
    # 收件人姓名
    user_recv = models.CharField(max_length=20, default='')

    # 创建自定义管理器类
    objects = UserManager()


# 用户浏览记录模型
class RecordBrowse(AbstractModel):

    # 浏览商品
    browse_goods = models.ForeignKey('goods.GoodsInfo')
    # 浏览者
    browse_user = models.ForeignKey('User')




























