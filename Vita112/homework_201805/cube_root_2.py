

# 定义一个求任意数g的立方根x的函数
def cube_root_2(g):
    # 规定x的初始值，精度以及计算次数
    x = 2*g/3 + g/(3*g*g)
    s, n = 0.01, 1

    # 当 x**3!= g 且 x**3-g结果大于要求精度时，求解过程
    while abs(x**3-g) >= s:
        x = 2*x/3 + g/(3*x*x)  # 牛顿迭代法
        print(x, n)
        n += 1
    return x

# 调用函数
answer = cube_root_2(-125)
print(answer)