# 输入一个数值，得到他的开方
# input 16 output 4
def sq(g):
    # x*x 比对 g 相等就返回，不相等就继续
    # (g/x + x)/2
    x = 3
    while True:
        if x*x == g:
            return x
        x = (g/x + x)/2

# g = int(input("input 16: "))
# x = sq(g)
# print(x)

