import random

#生成1-10中的一个数字作为答案
answer = random.randint(1, 10)

#比较输入的数字和答案
while True:
    #要求用户输入一个数字
    guess = input("please guess between 1 to 10: ")
    guess = int(guess)

    #相等的话，提示用户，你猜对了
    if guess == answer: 
        print("u are right")
        break
    #数字小于答案，提示用户，猜大一点
    if guess < answer:
        print("guess bigger")

    #数字大于答案，提示用户，猜小一点
    if guess > answer:
        print("guess smaller")

