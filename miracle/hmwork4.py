# 一个方法
# 两个参数，字符串x 字符串y
def get_str_location_in_an_str(x, y):
  # 判断x 是否存在与 y 中
  if x in y:
    # 是，返回x所在的位置
    return y.index(x) + 1
  # 返回-1
  return -1


answer = get_str_location_in_an_str('x', 'abcxyz') # 4
print(answer)
answer = get_str_location_in_an_str('x', 'yz') # -1
print(answer)