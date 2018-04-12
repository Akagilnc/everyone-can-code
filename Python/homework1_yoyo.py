import random

minimal = 1
maximal = 10
ran_num = random.randint(minimal, maximal)

information =  "please choose a number from {} to {} : " .format(minimal, maximal)
my_number = int(input(information))
x = 1

while True :
   if   my_number == ran_num :
        print("you got it at the {} time".format(x))
        break
   if   my_number > ran_num :
        print("smaller please")
   if   my_number < ran_num :
        print("larger please")
   x = x + 1
   my_number = int(input(information))
   if   my_number == ran_num :
        print("ÿou got it at the {} times.".format(x))
        break

