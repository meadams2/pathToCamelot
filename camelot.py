"""Marianne Adams
CS120
Path to Camelot"""
import pygame, simpleGE, random, camelotCharacter
    
class Tile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [pygame.image.load("grass.png"),
                       pygame.image.load("path.png"),
                       pygame.image.load("water.png"),
                       pygame.image.load("forest.png")]
        self.setSize(32, 32)
        self.stateName = ["grass", "path", "water", "forest"]
        self.GRASS = 0
        self.PATH = 1
        self.WATER = 2
        self.FOREST = 3
        self.state = self.GRASS
    
    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])

class Enemy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        enemy = camelotCharacter.Character()
        self.hitPoints = random.randint(0, 25)
        self.hitChance = random.randint(0, 100)
        self.maxDamage = random.randint(0, 15)
        self.healingFactor = random.randint(0, 100)
        self.maxHealing = random.randint(0, 15)
        self.armor = random.randint(0, 10)
        self.images = [pygame.image.load("Enemy1.png"),
                       pygame.image.load("Enemy2.png"),
                       pygame.image.load("Enemy3.png"),
                       pygame.image.load("Enemy4.png"),
                       pygame.image.load("Enemy5.png")]
        self.imagePos = random.randint(0, 4)
        self.copyImage(self.images[self.imagePos])
        self.x = random.randint(0, 640)
        self.y = random.randint(0, 480)

class Potion(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("healingPotion.png")
        self.x = random.randint(0,640)
        self.y = random.randint(0, 480)
        self.healthAdd = random.randint(0, 5)
 
class Rowan(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.rowan = camelotCharacter.Character("Rowan", 20, 25, 3, 10, 2, 5)
        self.setImage("RowanMain.png")
        self.position = (320, 240)
        self.moveSpeed = 2
        self.inventory = []
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
                
class LblHP(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "HP: 10"
        self.center = (100, 30)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("The Path to Camelot")
        self.tileset = []
        
        self.ROWS = 20
        self.COLS = 40
        
        self.SCREEN_ROWS = 10
        self.SCREEN_COLS = 10
        
        self.offRow = 0
        self.offCol = 0
        
        self.loadMap()
        
        self.hitPoint = 20
        self.lblHP = LblHP()
        
        self.rowan = Rowan(self)
        
        self.enemies = []
        for i in range(5):
            self.enemies.append(Enemy(self))
#             
        self.potions = []
        for i in range (4):
            self.potions.append(Potion(self))
            
        self.sprites = [self.tileset,
                        self.rowan,
                        self.enemies,
                        self.potions,
                        self.lblHP]
        
    def loadMap(self):
        self.map = [
    [1,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,2,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0,0,0,0,0,2,1,0,1,0,3,3,3,3,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,1,1,1,1,1,1,1,0,0,2,1,1,1,0,3,3,3,3,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,3,3,3,3,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,3,3,3,0,0,0,2,2,1,2,2,2,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,1,0,3,3,3,3,3,2,2,0,1,3,3,2,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,3],
    [0,0,1,0,3,3,3,3,2,2,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,3],
    [0,0,1,0,3,3,3,2,2,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,2,2,2,3],
    [0,0,1,0,3,3,2,2,0,0,0,0,1,0,3,2,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,0,0,0,0,3],
    [0,0,1,0,3,2,2,0,0,0,0,0,1,0,3,2,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [0,0,1,0,2,2,0,0,0,0,0,0,1,0,3,2,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,2,2,0,0,0,0,1,3],
    [0,0,1,2,2,1,1,1,1,1,1,1,1,0,3,3,2,1,2,3,3,3,3,3,1,0,0,0,0,0,2,2,2,0,0,0,0,0,1,3],
    [0,0,1,2,1,1,3,1,0,0,0,0,1,0,3,3,3,1,2,2,3,3,3,3,1,0,0,0,0,2,2,2,2,2,0,0,0,0,1,3],
    [0,1,1,1,1,3,3,1,0,0,0,0,1,0,3,3,3,1,3,2,2,2,2,2,1,0,0,2,2,2,0,0,0,2,2,2,0,0,1,3],
    [1,1,2,3,3,3,3,1,0,0,0,0,1,0,3,3,3,1,3,3,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,2,2,0,1,2],
    [0,1,1,3,3,3,3,1,0,0,0,0,1,0,3,3,3,1,3,3,2,2,2,2,1,2,2,0,0,0,0,0,0,0,0,0,2,2,1,2],
    [0,2,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,3,3,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,2,1,3],
    [2,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3]
]
        for row in range(self.ROWS):
            self.tileset.append([])
            for col in range (self.COLS):
                currentValue = self.map[row][col]
                newTile = Tile(self)
                newTile.setState(currentValue)
                xPos = 16 + (32 * col)
                yPos = 16 + (32 * row)
                newTile.x = xPos
                newTile.y = yPos
                self.tileset[row].append(newTile)
                
    def showMap(self):
        self.offRow = 0
        self.offCol = 0
        for row in range (self.SCREEN_ROWS):
            for col in range(self.SCREEN_COLS):
                currentVal = self.map[row + self.offRow][col + self.offCol]
                self.tileset[row][col].setState(currentVal)
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.offCol > 0:
                self.offCol -= 1
        
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.offCol < (self.COLS - self.SCREEN_COLS):
                self.offCol += 1
        
        if self.isKeyPressed(pygame.K_UP):
            if self.offRow > 0:
                self.offRow -= 1
        
        if self.isKeyPressed(pygame.K_DOWN):
            if self.offRow < (self.ROWS - self.SCREEN_ROWS):
                self.offRow += 1
        
        self.showMap()
        
    def fight(self):
        rowan.hit(enemy)
        enemy.hit(rowan)
        keepGoing = True
        while keepGoing:
            if enemy.hitPoints <= 0:
                enemies.remove()
                keepGoing = False
            elif rowan.hitPoints <= 0:
                rowan.hitPoints = 0
                game.stop()
                keepGoing = False
            else:
                enemy.hit(rowan)
                rowan.hit(enemy)
        self.lblHP.text = f"HP: {self.hitPoints}"
        
    def pickUp(self):
        for i in self.potions:
            if rowan.collideswith(potions):
                rowan.inventory.append(Potion())
    
    def heal(self):
        if Potion() in self.potions:
            rowan.hitPoints = potion.healthAdd
            rowan.inventory.remove(Potion())
        self.lblHP.text = f"HP: {self.hitPoints}"
    
    
                
    def characterProcess(self):
        if self.isKeyPressed(pygame.K_SPACE):
            for i in self.enemies:
                if rowan.collideswith(enemy):
                    self.fight()
        
        if self.isKeyPressed(pygame.K_a):
            for i in self.potions:
                if rowan.collideswith(potions):
                    self.pickUp()
                    
        if self.isKeyPressed(pygame.K_d):
            if Potion() in self.potions:
                self.heal()
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
