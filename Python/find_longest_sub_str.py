def find_longest_sub_str(input_str):
    start_i = 0
    result_list = []
    # 遍历从0到字符串的长度
    for i in range(len(input_str)):
        # 第一个字母进来的时候，并不需要去比较前一个字母，所以直接赋值并继续
        if i == 0 or input_str[i] > input_str[i - 1]:
            continue
        # 否则，把到目前为止的字符串存进LIST，然后继续
        else:
            result_list.append(input_str[start_i:i - 1])
            start_i = i

    # 把最后一个按照顺序排列的字母存入LIST
    result_list.append(input_str[start_i:len(input_str)])
    result_list.sort(key=lambda x: len(x))
    print('list is ', result_list)
    return result_list[-1]


print(find_longest_sub_str('abcbcdea'))
print(find_longest_sub_str('hgedabgjklgecegjkmnq'))
