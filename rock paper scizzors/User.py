class Player:
    def __init__(self, name, score, weapon):
        self.name = name
        self.score = 0
        self.weapon = ""

    def getName(self,name):
        return name
    
    def callWeapon(self, weapon):
        self.weapon = weapon
