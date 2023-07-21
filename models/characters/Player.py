class Player:
    def __init__(self, name, class_, life, weaponDmg):
        self.__name = name
        self.__class_ = class_
        self.__life = life
        self.__weaponDmg = weaponDmg


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_):
        self.__class_ = class_

    @property
    def weaponDmg(self):
        return self.__weaponDmg
    
    @weaponDmg.setter
    def weaponDmg(self, dmg):
        self.__weaponDmg = dmg
    
    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self, life):
        self.__life = life

    def lightAtk(self):
        return self.__weaponDmg

    def heavyAtk(self):
        return self.__weaponDmg * 1.30
