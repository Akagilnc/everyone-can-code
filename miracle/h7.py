##!/usr/bin/env python
# -*- coding: utf-8 -*-

# function 2
def finds(s1,s2):
    sum = 0
    for i in range (0,len(s2)):
        str = s2[i:]
        if(str.find(s1) == 0):
            sum +=1
        else:
            continue

s1 = 'bob'
s2 = 'azcbobobegghakl'
print (finds(s1,s2))




   



