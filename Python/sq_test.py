# 输入一个数字g
# 得到它的平方根
def sq(g):
    # 定义精度，定义step, 定义猜测平方根，定义次数
    epi, x, n = 0.0000000001, 1, 0
    low, high = 1, g
    # 如果 猜测平方根 ** 2 - g > 精度 重复执行下面的步骤
    while abs(x**2 - g) > epi:
        # 猜测平方根 += step
        
        x = (low + high)/2
        if (x**2 > g):
            high = x
        else: 
            low = x
        # 次数 += 1
        n += 1
        # 打印n 和 x
        print("guess {} times".format(n), low, high)

    # 输出我们的结果
    return x

sq(6553600000000)