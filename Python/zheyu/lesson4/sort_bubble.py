# 定义列表，[9, 5, 7, 4, 3]
ints = [9, 5, 7, 4, 3, 10, 1]
length = len(ints)
is_switch = True

# 当有交换发生，重复做以下步骤
while is_switch:
    # 遍历列表
    is_switch = False
    for index, value in enumerate(ints):
        print(index, value)
        # 如果 当前值大于下一个列表值
        if index < length - 1 and value > ints[index + 1]:
            # 互换位置
            ints[index], ints[index + 1] = ints[index + 1], value
            is_switch = True

# 列表
print(ints)

