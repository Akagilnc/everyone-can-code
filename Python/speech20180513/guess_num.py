import random


# 设置数字的范围与开始时的次数,生成正确答案
low, high, n = 1, 10, 1
answer = random.randint(low, high)
# 获取用户的输入，提示语为 Please input a integer between 1 to 10
guess_num = input('Please input a integer between {} to {}'.format(low, high))
guess_num = int(guess_num)
# 当没有猜中时。重复这些步骤
while guess_num != answer:
    # 如果用户猜的大了，提示他猜小点 Try guess smaller
    if guess_num > answer:
        print("Try guess smaller")
    # 如果用户猜的小了，提示他猜大点 Try guess greater
    else:
        print('Try guess greater')
    # 重新获取用户的输入
    guess_num = int(input())
    # 记录猜的次数，然后重新判断
    n += 1

# 如果用户在第一次以外的次数猜中，
if n != 1:
    # 提示You got it in x times
    print('You got it in {} times'.format(n))
# 否则
else:
    # 提示 You got it at the first time!!!
    print('You got it at the first time!!!')
    