#函数一：判断奇数和偶数
def number():
    num = int(input("input a number"))
    if num % 2 == 0 :
        return "it is a even"
    return "it is a odd number"