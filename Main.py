from entity.characters.PlayerMage import *
from entity.characters.PlayerWarrior import *

player = PlayerMage("vava", "mage", 50, 4)

print(player.name)

print(player.class_)

print(player.weaponDmg)

print(player.lightAtk())
print(player.heavyAtk())
