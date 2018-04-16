import random

minimal, maximal, x = 1, 10, 1
ran_num = random.randint(minimal, maximal)
information =  "please choose a number from {} to {} : " .format(minimal, maximal)
my_number = int(input(information))

if my_number == ran_num :
    print("you got it at the first time")

while my_number != ran_num :
    if   my_number > ran_num :
        print("smaller please")
    else:
        print("larger please")
    x += 1
    my_number = int(input(information))
    if   my_number == ran_num :
        print("you got it at the {} times.".format(x))
        break

