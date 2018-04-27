#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 输入一个数值，得到他的平方根
# 例如：input 16 output 4
def sq(g):
    # 从3开始猜测
    x = 3
    times = 1
    # 当x的平方不等于g时，重复执行以下步骤
    while abs(x**2 - g) > 0.0001:
        # 求平方根方法的公式 x = (g/x + x)/2 
        x = (g/x + x)/2
        times += 1
        print("guess {} times sq number = ".format(times) + str(x))
    
    # x*x 比对 g 相等时，返回结果
    return x


