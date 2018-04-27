import random

highest, lowest, i = 10, 0, 1

# 生成正确答案
answer = random.randint(lowest, highest)

# 获取用户的输入，提示语为Please input a integer between 1 to 10
info = "Please input a integer between {} to {}: ".format(lowest, highest)
guess = int(input(info))




while guess != answer:
    # 如果用户猜的大了，提示他猜小点
    if guess > answer:
        print('Try guess smaller. ')
    # 如果用户猜的笑了，提示他猜大点
    else:
        print('Try guess greater. ')
    # 重新获取用户的输入
    guess = int(input())
    # 记录猜的次数，重复
    i += 1

# 如果用户在第一次以外的次数猜中，提示You got it in x times
# 如果用户第一次猜中，提示You got it at the first time!!!
if i != 1:
    print('You got it in {} times.'.format(i + 1))
else:
    print("You got it at the first time!!!")
