#统计字符个数
def vowel_account(s):
    a_amount = s.count('a')
    i_amount = s.count('i')
    u_amount = s.count('u')
    e_amount = s.count('e')
    o_amount = s.count('o')
    vowels_account = a_amount + i_amount + u_amount + e_amount + o_amount
    return vowels_account
#测试程序
s = "azcbobobegghakl"
print(vowel_account(s))