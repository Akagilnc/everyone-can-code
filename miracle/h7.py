##!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计元音个数
def count_vowel(s):
    # 元音字母总个数
    count = 0
    for letter in s:
        if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
            count += 1
# 测试
s ='azcbobobegghakl'           
print ("numbers of vowels:" + count_vowel(s))

# 统计“bob次数”
def num_bob(str):
    result = [str[i:i+3] for i in range(len(str)-2)]
    return result.count('bob')
# 测试
str = 'azcbobobegghakl'
print ("Number of times bob occurs is :" + num_bob(str))

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
s1 = 'azcbobobegghakl' 
print ("Longest substring in alphabetical order is: " + longest_substring(s))
s2 = 'abcbcd'  
print ("Longest substring in alphabetical order is: " + longest_substring(s))
   



