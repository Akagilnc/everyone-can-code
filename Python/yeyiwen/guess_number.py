import random

# 设置数字的范围与开始时的次数,生成正确答案
low, high, x = 1, 10, 1
answer = random.randint(low, high)
# 获取用户的输入，提示语为 Please input a integer between 1 to 10
input_number = int(input("Please input a integer between {} to {}: ".format(low, high)))
# 当没有猜中时。重复这些步骤
while answer != input_number:
    # 如果用户猜的大了，提示他猜小点 Try guess smaller
    if input_number > answer:
        print("Try guess smaller")
    # 如果用户猜的小了，提示他猜大点 Try guess greater
    else:
        print("Try guess greater")
    # 重新获取用户的输入
    input_number = int(input())
    # 记录猜的次数，然后重新判断
    x += 1

# 如果用户在第一次以外的次数猜中，
if x > 1:
    # 提示You got it in x times
    print('you got it in {} times'.format(x))
# 否则
else:
    # 提示 You got it at the first time!!!
    print("you got it at the first time!!!")
