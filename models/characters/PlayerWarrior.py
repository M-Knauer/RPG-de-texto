from models.characters.Player import *

class PlayerWarrior(Player):
    def __init__(self, name, class_, life, weaponDmg):
        super().__init__(name, class_, life, weaponDmg)

    def lightAtk(self):
        print("*Cross section*")
        return super().lightAtk()
    
    def heavyAtk(self):
        print("*Sword swirl*")
        return super().heavyAtk()