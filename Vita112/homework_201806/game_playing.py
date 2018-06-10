from Vita112.homework_201806.game_roles import Human as human
from Vita112.homework_201806.game_roles import Fairy as fairy
from Vita112.homework_201806.game_roles import Dwarf as dwarf
from Vita112.homework_201806.game_weapon import Weapon as weapon

# 创建游戏角色可能使用的5种武器
long_sword = weapon('sword', 'long_sword', 1500, 1000)
Hammer = weapon('hammer', 'hammer', 1800, 1000)
Ax = weapon('ax', 'ax', 2000, 1500)
fairy_bow = weapon('long_distance_weapon', 'greater_bow', 1200, 800)
dwarf_bow = weapon('long_distance_weapon', 'smaller_bow', 1000, 600)

# 创建游戏中的3个角色
Edward = human('Edward', 'prince', '1000', '500', long_sword)
Angela = fairy('Angela', 'Guardian Angel', 1500, 2000, weapon=fairy_bow)
Sleepy = dwarf('Sleepy', 'servant', 500, dwarf_bow)
print(Sleepy.weapon.name)
