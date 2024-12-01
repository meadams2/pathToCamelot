"""Marianne Adams
CS120
Path to Camelot
Character Module"""
import random

def main():
    villain = Character("Villain", 10, 10, 5, 10, 3, 0)
    hero = Character()
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.healingFactor = 20
    hero.maxHealing = 2
    hero.armor = 2
    hero.printStats()
    villain.printStats()
    hero.hit(villain)
    villain.hit(hero)
    
class Character(object):
    def __init__(self, name = "Billy Bob John", hitPoints = 10, hitChance = 30, maxDamage = 3, healingFactor = 20, maxHealing = 4, armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.healingFactor = healingFactor
        self.maxHealing = maxHealing
        self.armor = armor
#         self.healingPower = healingPower
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
        return out
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = self.testInt(value, 0, 10000, 1)
        return self.__maxDamage
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            self.__hitPoints = value
        else:
            print("HP must be an integer.")
            self.__hitPoints = 10
        return self.__hitPoints
    
    @property
    def hitChance(self):
        return self.__hitChance
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = self.testInt(value, 0, 100, 0)
        return self.__hitChance
    
    @property
    def healingFactor(self):
        return self.__healingFactor
    @healingFactor.setter
    def healingFactor(self, value):
        self.__healingFactor = self.testInt(value, 0, 100, 0)
        return self.__healingFactor
    
    @property
    def maxHealing(self):
        return self.__maxHealing
    @maxHealing.setter
    def maxHealing(self, value):
        self.__maxHealing = self.testInt(value, 0, 10000, 1)
        return self.__maxHealing
    
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self, value):
        self.__armor = self.testInt(value, 0, 1000, 0)
        return self.__armor
    
#     @property
#     def healingPower(self):
#         return self.__healingPower
#     @healingPower.setter
#     def healingPower(self, value):
#         self.__healingPower = self.testInt(value, 0, self.maxHealing, 0)
#         return self.__healingPower
    
    def printStats(self):
        print(f"""{self.name}

HP: {self.hitPoints}
Hit Chance: {self.hitChance}
Max Damage: {self.maxDamage}
Healing Factor: {self.healingFactor}
Max Healing: {self.maxHealing}
Armor: {self.armor}""")
        
    def hit(self, enemy):
        if random.randrange(1, 100) <= self.hitChance:
            hitDamage = random.randrange(1, self.maxDamage)
            hitDamage -= enemy.armor
            if random.randrange(1, 100) <= self.healingFactor:
                self.healingPower = random.randrange(1, self.maxHealing)
#                 hitDamage -= enemy.healingPower
                if hitDamage < 0:
                    hitDamage = 0
                enemy.hitPoints -= hitDamage
            else:
                hitDamage = 0
                enemy.hitPoints -= hitDamage
            print (f"{hitDamage} - {enemy.hitPoints}")
            return enemy.hitPoints
main()  