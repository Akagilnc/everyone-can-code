##!/usr/bin/env python
# -*- coding: utf-8 -*-

# function 1
def even_odd(a):
    # 判断a是否为偶数
    if a % 2 == 0:
        # 返回“it's an even"
        return "it's an even" 
    #返回“it's an odd"
    return "it's an odd number"

# function 2
def string_valid(sentence):
    # 判断是否为字符串
    if type(sentence) == str :
        #返回字符串的长度
        return len(sentence)
    #返回“invalid string”
    return "invalid string"
    
# fuction 3
def cube_root(g):
    # 定义精度
    epi = 0.00001
    low, high = 1, g
    x = (low + high)/2
    while abs(x**3 - g) < epi:

        if (x**3 > g):
            high = x
        else: 
            low = x
         # 次数 += 1
        x += 1
    #返回 x
    return 

g=(9)


       




