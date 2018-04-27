import random

min_number, max_number = 1, 10
random_number = random.randint(min_number, max_number)

warning = 'Please input a  number whose limit is {} to {} : '.format(min_number, max_number)

my_number = int(input(warning))
your_guess_is_large = 'smaller please'
your_guess_is_small = 'greater please'
first_success = 'you got it at the first time'
x = 1


while True:
    if  my_number == random_number:
        print(first_success)
        break
    if my_number > random_number:
        print(your_guess_is_large)
    if my_number < random_number:
        print(your_guess_is_small)
    x = x + 1
    x_success = 'you got it at the {} times'.format(x)
    my_number = int(input(warning))
    if my_number == random_number:
        print(x_success)
        break




