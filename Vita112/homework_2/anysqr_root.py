

# 定义一个求任意数g的任意方根x的函数
def anysqr_root(g, r):

    # 设置计算精度s，计算次数n, x初始值
    s, n = 0.00000000001, 1
    x = (r-1)*g/r + g/(r*g**(r-1))
    # 当 x**r!= g 且 x*r-g 的结果大于要求精度时，求解过程
    while abs(x**r-g) >= s:
        x = (r-1)*x/r + g/(r*x**(r-1))  # 这个公式我也是一知半解，求讲解。
        print(x, n)
        n += 1
    # 返回待求值x
    return x


# 调用函数，输入结果
print(anysqr_root(9, 2))