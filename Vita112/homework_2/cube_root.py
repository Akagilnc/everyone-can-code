

# 申明：老斯，这是一个错误的答案，但是我不知道为啥？？？
# 定义一个求任意数g的立方根x的函数
def cube_root(g):
    # 设置计算结果精度s，计算次数n，
    s, n, = 0.01, 1

    # 当任意数g为非负数时
    if g >= 0:
        # 规定x的初始值，值获取范围low，high
        x, low, high =1, 0, g
        # 当x**3 != g时的计算过程
        while abs(x**3 - g) >= s:
            x = (low + high)/3
            # 利用二分搜索法计算x
            if x**3 > g:
                high = x
            else:
                low = x
            print(x, n)
            n += 1

    # 当任意数g为负数时
    if g <0:
        # 规定x的初始值，值获取范围low，high
        x, low, high =0, g, 0
        # 当x**3 != g时的计算过程
        while abs(x ** 3 - g) >= s:
            x = (low + high) / 3
            # 利用二分搜索法计算x
            if x ** 3 < g:
                low = x
            else:
                high = x
            print(x, n)
            n += 1
    # 返回待求值x
    return x

# 调用函数，输入结果
cube_root(-25)