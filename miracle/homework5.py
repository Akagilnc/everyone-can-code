# 如果是偶数那么除于 2 余数为 0
# 如果余数为 1 则为奇数
 
num = int(input("数字: "))
if (num % 2) == 0:
    print("it's an even")
else:
    print("it's an odd")