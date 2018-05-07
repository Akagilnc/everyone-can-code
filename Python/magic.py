#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 魔术师名字列表
names = ['niclose', 'mickle', 'mikky', 'maggy']


# 函数：打印所有的魔术师名字
def show_magicians(names):
    # 取出列表中每一个名字
    for name in names:
        # 打印
        print(name)


# 函数：把所有名字前面加上 'the great'  在调用 SHOW 函数打印
def make_great(names, temp_str):
    # 取出每一个名字
    result = []
    for name in names:
        # 在前面加上'the great'
        name = temp_str + name
        # 储存结果
        result.append(name)
    return result


result = make_great(names, 'the biggest ')
show_magicians(result)