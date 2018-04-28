#函数一：判断奇数和偶数
def number():
    num = int(input("input a number"))
    if num % 2 == 0 :
        return "it is a even"
    return "it is a odd number"
#函数二：计算字符串长度
def length(abc):
     var = "abc"
     if type(var) == str :
         return length(var)
     else :
         return "invalid string"
#函数三：利用穷举法计算立方根
def cube():
#列出初始数字，每次的变量，精度
     basic, x, y,number = 1, 0.001, 0.0001, 8
#计算和比较
     if abs(number - basic**3) > y :
         basic += 1
     else :
         return basic







