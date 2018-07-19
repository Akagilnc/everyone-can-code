

# 定义一个打印指定字符串str_mom中，最长的按照字母表顺序顺排的子字符串的函数print_longest_substr
def print_longest_substr(str_mom):

    ''' 当字母letter2在字母表中的位置在前一个字母letter1之后时，以letter1为起点向后查找，
        当发现letter2在letter1之前时，打印次一次查找结果；按照之前的规则继续查找 '''

    str_sub_list = []
    start_i = 0
    # 从第一个字母开始，遍历字符串的字母
    for i in range(len(str_mom)):
        # 以下2种情况时，遍历继续：当i为第一个字母时；当后一个字母小于前一个字母时
        if i == 0 or str_mom[i] > str_mom[i-1]:
            continue
        else:
            str_sub_list.append(str_mom[start_i:i-1])  # 将符合条件的字符串添加到str_sub_list
            start_i = i

    str_sub_list.append(str_mom[start_i:len()])
    result = str_sub_list.sort(key=lambda x:len(x))

    return result[-1]


# 获取输入的小写英文字母字符串
str1 = input('请输入一组小写英文字母： ')

# 调用函数
print(print_longest_substr(str1))
