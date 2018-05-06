#统计元音个数
def vowel_account(s):
    a_amount = s.count('a')
    i_amount = s.count('i')
    u_amount = s.count('u')
    e_amount = s.count('e')
    o_amount = s.count('o')
#计算元音总数
    vowels_account = a_amount + i_amount + u_amount + e_amount + o_amount
    return vowels_account
#测试程序
s = "azcbobobegghakl"
print ("Number of vowels:" , vowel_account(s) )

#统计小写字符串个数
#因为要重复计算Bob的个数，所以引入了正则表达式
import re
def times_of_bob(s):
    reg = re.compile('(?=bob)')
    bob_account = len(reg.findall(s))
    return bob_account
#测试程序
s = "azcbobobegghakl"
print ("Number of times bob occurs is :" , times_of_bob(s))


