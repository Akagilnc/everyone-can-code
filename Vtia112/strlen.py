#定义一个返回字符串长度的函数
def strlen(s):

    if isinstance(s, str) :
        print('该字符串的长度为：%d' % len(s))
    else:
        print('Invalid string.')


#获取用户输入
#isstr= input('请输入一个字符串： ')
var = 24324321
#调用函数
strlen(var)