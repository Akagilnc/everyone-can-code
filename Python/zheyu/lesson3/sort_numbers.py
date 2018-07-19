number_list = []

for x in range(1, 10):
    temp = int(input("please input a number: "))
    number_list.append(temp)

number_list.sort(reverse=True)
print(number_list)
number_sum = 0
for number in number_list:
    number_sum += number

print(number_sum)
