# 接受一个英文名字规则命名的姓名
# Houjing Wei


def change_name(input_name='Houjing Wei'):
    # 做一些处理,根据空格切割字符串，对调位置
    temp = input_name.split(" ")

    # 把姓放到前面，加空格，加名字
    name = temp[1] + " " + temp[0]
    # 输出一个中文名字命名的姓名
    # Wei Houjing
    return name


def revert(input_str='abcde'):
    # 从最后开始取，到第一个字母，步数为-1
    return input_str[-1::-1]






