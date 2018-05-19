

# 定义一个求任意数g的任意方根x的函数
def anysqr_root(g, r):
    is_positive = True
    if g >= 0 and r % 2 == 0:
        is_positive = True
        g = g
    elif g < 0 and r % 2 != 0:
        is_positive = False
        g = 0 - g
    else:
        print('The square root of this number can\'t be extracted.')

    # 设置计算精度s，计算次数n, x取值范围及其初始值
    s, n = 0.0001, 1
    low, high = 0, g
    x = (low + high)/2
    # x = (r-1)*g/r + g/(r*g**(r-1))  牛顿迭代法
    # 当 x**r!= g 且 x*r-g 的结果大于要求精度时，求解过程
    while abs(x**r - g) >= s:
        if x**r > g:
            high = x
        else:
            low = x
        print(x, n)
        n += 1
        x = (low + high) / 2
    #   x = (r-1)*x/r + g/(r*x**(r-1))  #
    #   print(x, n)
    #   n += 1
    # 返回待求值x
    if is_positive:
        return x
    else:
        return 0 - x


# 调用函数，输入结果
print(anysqr_root(-25, 3))