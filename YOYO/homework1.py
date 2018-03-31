import random

minimal = 1
maximal = 10
ran_num = random.randint(minimal, maximal)

information =  "please choose a number from {} to {} : " .format(minimal, maximal)
my_number = int(input(information))

if my_number == ran_num :
   print("you got it at the first time")
