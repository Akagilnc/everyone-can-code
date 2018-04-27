#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sq(g):
    # 获取用户的输入g
    # 设置初始猜测的平方根为x = 3
    epi = 0.0001
    x, n = 3, 1
    # 当x的平方不等于g时，重复以下步骤
    while abs(x**2 - g) > epi:
        # 求平方根的公式，x = (g/x + x)/2
        x = (g/x + x)/2
        print("guess {} times".format(n), x)
        n += 1
    # 返回x
    return x


sq(6553600000000)
