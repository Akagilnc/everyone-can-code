##!/usr/bin/env python
# -*- coding: utf-8 -*-

# 搞了半天还是无法运行程序，一直找不到文件，也没法验证检查。我先上传了，再琢磨下再改。
# function 1
def stats_vowel(s):
    s = 'azcbobobegghakl'
    num = 0
    for s in 'aeiou':
        num +=1
print ("numbers of vowels:" + str(num))

# function 2
def finds(s1,s2):
    sum = 0
    for i in range (0,len(s2)):
        str = s2[i:]
        if(str.find(s1) == 0):
            sum +=1
        else:
            continue
# 测试
s1 = 'bob'
s2 = 'azcbobobegghakl'
print (finds(s1,s2))

# function 3
def max_sub(s):
    cont =[]
    sub =[]
    for i in s :
        if len(sub) >=1 and lowercase.index(sub[-1]) <= lowercase.index(i):
            sub.append(i)
            cont.append(''.join(sub))
        else:
            sub = []
            sub.append(i)
    # print cont
    cont = sorted(cont,key=len,reverse=True)
    return cont [0]

# 测试
s1 = 'azcboboegghakl'
s2 ='abcdcd'
result 1 = max_sub(s1)
print "longest subsrting of "azcboboegghakl" in alphabetival order is "begg" (s1,result1)
result 2 = max_sub(s2)
print "longest subsrting of "abcdcd" in alphabetival order is "abc" (s2,result2)



   



