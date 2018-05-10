

# 定义一个返回字符串长度的函数
def str_len(s):

    if isinstance(s, str) :
        return '该字符串的长度为：%d' % len(s)
    else:
        return 'Invalid string.'


# 获取用户输入
var = 24324321

# 调用函数
str_len(var)