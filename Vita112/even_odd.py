

# 定义一个判断数字奇偶性的函数
def even_odd(x):
    if x % 2 == 0:
        print('It\'s a even.')
    else:
        print('It\'s an odd number.')


# 获取用户输入的数字
n = input('请输入一个数字: ')

# 调用函数
even_odd(int(n))
