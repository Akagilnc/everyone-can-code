

# 定义一个求任意数g的立方根x的函数
def cube_root(g):
    is_positive = True
    if g < 0:
        is_positive = False
        g = 0 - g
    # 设置计算结果精度s，计算次数n，
    s, n, = 0.01, 1

    # 规定x的初始值，值获取范围low，high
    low, high = 0, g
    x = (low + high) / 2

    # 当 x**3 != g 时的计算过程
    while abs(x**3 - g) >= s:
        # 利用二分搜索法计算x
        if x**3 > g:
            high = x
        else:
            low = x
        print(x, n)
        n += 1
        x = (low + high) / 2

    # 返回待求值x
    if is_positive:
        return x
    else:
        return 0 - x

# 调用函数，输入结果
cube_root(-125)