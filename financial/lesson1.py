import random

def even_or_odd(number):

    # 如果是偶数，输出，是偶数
    if int(number) % 2 == 0:
        print("It's an even")
        return "even"

    # 否则，输出是奇数
    else:
        print("It's an odd")
        return "odd"


def guess_game():
    # 设置数字的范围与开始时的次数,生成正确答案
    lowest, highest, times = 1, 10, 1
    answer = random.randint(lowest, highest)
    # 获取用户的输入，提示语为 Please input a integer between 1 to 10
    input_num = input('Please input a integer between {} to {}: '.format(lowest, highest))
    input_num = int(input_num)
    # 当没有猜中时。重复这些步骤
    while input_num != answer:
        # 如果用户猜的大了，提示他猜小点 Try guess smaller
        if input_num > answer:
            print("Try guess smaller")
        # 如果用户猜的小了，提示他猜大点 Try guess greater
        else:
            print("Try guess greater")
        # 重新获取用户的输入
        input_num = int(input())
        # 记录猜的次数，然后重新判断
        times += 1
    # 如果用户在第一次以外的次数猜中，
    if times > 1:
        # 提示You got it in x times
        print("You got it in {} times".format(times))
    # 否则
    else:
        # 提示 You got it at the first time!!!
        print("You got it at the first time!!!")


