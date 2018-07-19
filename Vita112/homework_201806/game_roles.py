

# 创建三个类，用于描述游戏中出现的三个角色
class Human:
    name, job, hp, mp, weapon = '', '', 0, 0, ''

    def __init__(self, name, job, hp, mp, weapon):
        self.name = name
        self.job = job
        self.hp = hp
        self.mp = mp
        self.weapon = weapon


class Fairy:
    name, job, hp, mp, weapon = '', '', 0, 0, ''

    def __init__(self, name, job, hp, mp, weapon):
        self.name = name
        self.job = job
        self.hp = hp
        self.mp = mp
        self.weapon = weapon


class Dwarf:
    name, job, hp, weapon = '', '', 0, ''

    def __init__(self, name, job, hp, weapon):
        self.name = name
        self.job = job
        self.hp = hp
        self.weapon = weapon