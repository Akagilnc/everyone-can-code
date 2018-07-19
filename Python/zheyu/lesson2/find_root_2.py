# 获取用户的输入g
g = int(input("please input a number: "))
times = 1
# 设置初始猜测的平方根为x = 1 , 误差值p = 0.00001
x, p = 1, 0.00001
# 当x的平方 - g的绝对值 大于或等于 p，重复以下步骤
left, right = 1, g
while abs((x**2 - g)) >= p:
    print(times, x)
    x = (right + left) / 2
    # 判断 X ** 2 > g
    if x**2 > g:
        # 范围是左边
        right = x
    # 否则
    else:
        # 范围在右边
        left = x

    times += 1

# 返回x
print(times, x)
