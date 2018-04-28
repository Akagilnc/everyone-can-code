#函数一：判断奇数和偶数
def number():
    num = int(input("input a number"))
    if num % 2 == 0 :
        return "it is a even"
    return "it is a odd number"
#函数二：计算字符串长度
def length():
     var = "Have fun"
     if type(var) == str :
         return length(var)
     else :
         return "invalid string"




