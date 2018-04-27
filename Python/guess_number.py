import random

# 设置数字的范围与开始时的次数,生成正确答案
lowest, highest, times = 1, 10, 1
answer = random.randint(lowest, highest)
# 获取用户的输入，提示语为 Please input a integer between 1 to 10
number = input("Please input a integer between 1 to 10: ")
number = int(number)
# 当没有猜中时。重复这些步骤
while number != answer:
    # 如果用户猜的大了，提示他猜小点 Try guess smaller
    if number > answer:
        print("Try guess smaller ")
    # 如果用户猜的笑了，提示他猜大点 Try guess greater
    else:
        print("Try guess greater")
    # 重新获取用户的输入
    number = int(input())
    # 记录猜的次数，然后重新判断
    times += 1

# 如果用户在第一次以外的次数猜中，
if times != 1:
    # 提示You got it in x times
    print("You got it in {} times".format(times))
# 否则
else:
    print("You got it at the first time!!!")
    # 提示 You got it at the first time!!!