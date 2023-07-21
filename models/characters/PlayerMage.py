from models.characters.Player import *

class PlayerMage(Player):
    def __init__(self, name, class_, life, weaponDmg):
        super().__init__(name, class_, life, weaponDmg)

    def lightAtk(self):
        print("*Fire ball*")
        return super().lightAtk()
    
    def heavyAtk(self):
        print("*Meteor shower*")
        return super().heavyAtk()