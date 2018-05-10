

# 定义一个判断字符串是否包含子串的函数
def find_str(s, t):
    if t in s:
        result = s.find(t)
        return result
    else:
        return -1


# 设置3个字符串，要求2个子串中，1个在母字符串中，1个不在。
str1 = 'The best way of keeping a secret is to pretend there is not one.'
str2 = 'keeping a secret'
str3 = 'No one keeps no secrets.'

# 调用函数
find_str(str1,str3)
find_str(str1,str2)


