import random

highest, lowest, i = 10, 0, 1
answer = random.randint(lowest, highest)
info = "Please input a intellage between {} to {}: ".format(lowest, highest)
guess = int(input(info))

if guess == answer:
    print("You got it at the first time!!!")

while guess != answer:
    if guess > answer:
        print('Try guess smaller. ')
    else:
        print('Try guess greater. ')
    guess = int(input())
    i += 1

print('You got it in {} times.'.format(i + 1))
