

# 求平方根的函数
# 待求平方根g的数字的输入
# 输出g的平方根X
# 如果 X的平方根 与 G的差异小于0。0001，我们就认为X是G的平方根
def sq(g):
    # step1 设置X的初始值
    # s 是我们可以接受的精度 n是计算的次数
    s, n = 0.01, 1
    # 范围
    low, high = 1, g
    # x是我们每次猜测的平方根
    x = 1
    # step2 x*x != g 需要继续求平方根
    while abs(x**2 - g) >= s:
        x = (low + high) / 2
        n += 1

        if x**2 > g:
            high = x
        else:
            low = x

        print(x, n)

    # step3 x*x = g 返回结果
    return x


print(sq(100))
