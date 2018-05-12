

# 定义一个计算待求数g的平方根x的函数
def sq_cal(g):
    # 规定开方根的精度，x的初始值，确定待求值的获取范围
    s, n, x = 0.01, 1, 1
    low, high = 0, g
    # 设置函数出口
    while abs(x**2 - g) >= s:
        x = (low + high) / 2
    # 使用二分搜索算法，规定g的开方根在精度外时的计算方法
        if x**2 > g:
            high = x
        else:
            low = x
        print(x, n)
        n += 1
    return x


# 调用函数，输出结果
print(sq_cal(9))