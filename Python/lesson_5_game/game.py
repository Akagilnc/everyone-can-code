import Python.lesson_5_game.person as person
import Python.lesson_5_game.weapon as weapon

long_sword = weapon.Sword(att=120, defence=50, name='Long_Sword')
Lucy = person.Person(name='Lucy', hp=0, job='Knight', weapon=long_sword, mp=0)
print(Lucy.weapon.attack)

print(Lucy.name, Lucy.job, Lucy.hp, Lucy.weapon.name)
print(Lucy.weapon)