##!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计元音个数
def num_of_vowels(s):
    count = 0
    # 利用in的方法查找字符串中元音的数量
    for letter in s:
        if letter in 'aeiou':
            count += 1
    return count
# 测试
s ='azcbobobegghakl'           
print ("Numbers of vowels: " , num_of_vowels(s))

# 统计“bob次数”
def num_bob(str):
    count = 0
    # range（）方法，当i大于0小于字符串s的长度的时候
    for i in range (0,len(str)):
        # 如果从str中截取3位字母长度的子串，当等于‘bob’时，将计数加1
        if str[i:i+3] == 'bob' :
            count += 1
    return count 
# 测试
str = 'azcbobobegghakl'
print ("Number of times bob occurs is: " , num_bob(str))

# 最长字符
def longest_substring(s):
    in_orders = ['' for i in range(len(s))]
    index = 0
    for i in range(len(s)):
        if (i == len(s) - 1 and s[i] >= s[i - 1]) or s[i] <= s[i + 1]:
            in_orders[index] += s[i]
        else:
            in_orders[index] += s[i]
            index += 1
    return max(in_orders, key=len)  
# 测试
s = 'azcbobobegghakl' 
print ("Longest substring in alphabetical order is: " , longest_substring(s))
s = 'abcbcd'  
print ("Longest substring in alphabetical order is: " , longest_substring(s))
   


