# 获取用户的输入g
g = int(input("input a number to sq: "))
# 设置初始猜测的平方根为x = 3
x = 3
# 当x的平方不等于g时，重复以下步骤
while x*x != g:
    # 求平方根的公式，x = (g/x + x)/2
    x = (g / x + x) / 2
    print(x)
# 返回x
print(x)