import random
# 准备需要的各种数据与信息
def init():
    minimal, maximal, x = 1, 10, 1
    ran_num = random.randint(minimal, maximal)
    information =  "please choose a number from {} to {} : " .format(minimal, maximal)
    return minimal, maximal, x, ran_num, information

# 接收用户的猜测，返回猜测的结果
def guess(guessNum, answerNum, times):

    # 猜中的两种情况，第一次与第N次
    if guessNum == answerNum:
        if times == 1:
            return "you got it at the first time", True
        return "you got it at the {} times.".format(times), True 

    #猜错的两种情况，大了和小了
    if   guessNum > answerNum :
        return "smaller please", False
    else:
        return "larger please", False

# 获得用户的猜测的输入
def get_user_guess(information):
    return int(input(information))


def guess_game():
    min_num, max_num, times, answer, info = init()

    while True:
        guessNum = get_user_guess(information=info)

        result, flag = guess(guessNum, answer, times)

        print(result)

        if flag:
            break

        times += 1


