
from Vita112.homework_201806.game_weapon import Weapon as Weapon

# weapon = weapon()


# 创建类，描述游戏角色的动作-进攻和防守
class Movement:

    def __init__(self, movement_type, weapon):
        self.movement_type = movement_type
        self.weapon = weapon
        self.moving_right = True
        self.moving_left = True

    def movement(self, weapon):
        self.weapon = Weapon('', '', 0, 0)
        # 当角色进攻时，返回武器的进攻值
        if self.moving_right:
            return weapon.att
        # 当角色防守时，返回武器的防守值
        elif self.moving_left:
            return weapon.defence
        else:
            return -1


long_sword = Weapon('sword', 'long_sword', 1500, 1000)
moving_left = Movement('moving_up', long_sword)
print(Movement.movement(moving_left, long_sword))



