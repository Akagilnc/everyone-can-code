

# 定义一个统计字符串str中,指定字符串str_temp的数量的函数count_particular_str
def count_particular_str(str, str_particular):

    if str_particular in str:
        result = 0
        for i in range(len(str)):
            if str[i:i+len(str_particular)] == str_particular:
                result += 1
    else:
        return -1

    return result




# 获取输入的小写英文字母字符串
str1 = input('请输入一组小写英文字母： ')
str2 = input('请输入另外一组小写英文字母： ')

# 调用函数
print(count_particular_str(str1, str2))