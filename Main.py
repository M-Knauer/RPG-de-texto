from models.characters.PlayerMage import *
from models.characters.PlayerWarrior import *
from models.characters.Enemy import *
from tools.dice import dice

player = PlayerMage("vava", "mage", 50, 4)

print(player.name)
print(player.class_)
print(player.weaponDmg)
print(player.lightAtk())
print(player.heavyAtk())
print(dice())

enemy = Enemy("Spider", 500, 10)

print(enemy.name)
print(enemy.life)
print(enemy.weaponDmg)
print(enemy.lightAtk())
print(enemy.heavyAtk())
