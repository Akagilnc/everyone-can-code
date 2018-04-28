#函数一：判断奇数和偶数
def number(num):
    if num % 2 == 0 :
        return "it is a even"
    return "it is a odd number"
#函数二：计算字符串长度
def length(var):
     if type(var) == str :
         return int(len(var))
     else :
         return "invalid string"
#函数三：利用穷举法计算立方根
def cube(number):
#列出初始数字，每次的变量，精度
     basic, x, y = 1, 0.001, 0.0001
#计算和比较
     while abs(number - basic**3) > y :
         basic += 1
     else :
         return int(basic)
#测试程序运行
num = int(input("input a number :"))
print(number(num))

var = "hello"
print(length(var))

number = 8
print(cube(number))







