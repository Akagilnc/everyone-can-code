

# 定义一个统计字符串str中的元音数量的函数count_vowels

def count_vowels(str):
    result = [ ]
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in str:
        if letter in vowels:
            result.append(letter)

    return len(result)

# 获取输入的小写英文字母字符串
temp_str = input('请输入一组小写英文字母： ')

# 调用函数
print(count_vowels(temp_str))

