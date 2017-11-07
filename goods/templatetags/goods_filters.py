from django.template import Library


register = Library()


# 创建过滤器
def create_imgage_name(index):
    return 'images/banner0' + str(index) +'.jpg'

def convert_str_to_int(my_str):
    return int(my_str)


register.filter('create_imgage_name', create_imgage_name)
register.filter('convert_str_to_int', convert_str_to_int)