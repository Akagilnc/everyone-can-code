#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sq(g):
    # 获取用户的输入g
    # 设置初始猜测的平方根为x = 3
    x = 3
    # 当x的平方不等于g时，重复以下步骤
    while x**2 != g:
        # 求平方根的公式，x = (g/x + x)/2
        x = (g/x + x)/2
    # 返回x
    return x



