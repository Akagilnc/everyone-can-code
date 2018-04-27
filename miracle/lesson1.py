input_number = input()
input_number = int(input_number)


# 希望输入一个数字，返回这个数字的平方根
def sq(x):
    # 猜测一个数字g
    g = 3

    while True:
        # 比较g*g 是否等于 x
        if g * g == x:
            # 如果相等，返回结果g
            return g

        # 如果不等于g=(x/g + g)/2
        g = (x / g + g) / 2


print(sq(input_number))
