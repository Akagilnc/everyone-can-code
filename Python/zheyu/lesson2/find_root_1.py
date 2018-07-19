# 获取用户的输入g
g = int(input("please input a number: "))
times = 1
# 设置初始猜测的平方根为x = 3 , 误差值p = 0.00001
x, p = 3, 0.00001
# 当x的平方 - g的绝对值 大于或等于 p，重复以下步骤
while abs((x**2 - g)) >= p:
    print(times, x)
    # 求平方根的公式，x = (g/x + x)/2
    x = (g / x + x) / 2
    times += 1

# 返回x
print(times, x)
