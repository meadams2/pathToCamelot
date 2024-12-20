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
        self.char = camelotCharacter.Character()
        self.char.hitPoints = random.randint(0, 20)
        self.char.hitChance = random.randint(0, 100)
        self.char.maxDamage = random.randint(0, 10)
#         self.char.healingFactor = random.randint(0, 100)
        self.char.armor = random.randint(0, 5)
        self.images = [pygame.image.load("Enemy1.png"),
                       pygame.image.load("Enemy2.png"),
                       pygame.image.load("Enemy3.png"),
                       pygame.image.load("Enemy4.png"),
                       pygame.image.load("Enemy5.png")]
        self.imagePos = random.randint(0, 4)
        self.copyImage(self.images[self.imagePos])
        self.x = random.randint(0, 640)
        self.y = random.randint(0, 480)

# class Potion(simpleGE.Sprite):
#     def __init__(self, scene):
#         super().__init__(scene)
#         self.setImage("healingPotion.png")
#         self.x = random.randint(0,640)
#         self.y = random.randint(0, 480)
#         self.healthAdd = random.randint(0, 5)
        
class Rowan(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.char = camelotCharacter.Character()
        self.char.hitPoints = 20
        self.char.hitChance = 40
        self.char.maxDamage = 5
        self.char.armor = 5
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
#         self.font = "Viner ITC"
        self.bgColor = "white"
        self.fgColor = "black"
        self.text = f"HP: 10"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
#         self.font = "Viner ITC"
        self.bgColor = "white"
        self.fgColor = "black"
        self.text = f"Time Left: 10:00:00"
        self.center = (500, 30)
class Elixir(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("elixirSprite.png")
        self.position = (600, 275)
        
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

        self.rowan = Rowan(self)
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 60
        self.lblTime = LblTime()
        
        self.lblHP = LblHP()
        self.lblHP.text = f"HP: {self.rowan.char.hitPoints}"
        
        self.elixir = Elixir(self)
        
        self.enemies = []
        for i in range(3):
            self.enemy = Enemy(self)
            self.enemies.append(self.enemy)
#         self.potions = []
#         for i in range (4):
#             self.potion = Potion(self)
#             self.potions.append(self.potion)
            
        self.sprites = [self.tileset,
                        self.rowan,
                        self.elixir,
                        self.enemies,
                        self.lblHP,
                        self.lblTime]
        
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
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft(): .2f}"
        if self.isKeyPressed(pygame.K_SPACE):
            for enemy in self.enemies:
                if self.rowan.collidesWith(enemy):
                    self.fight()
                    
        if self.timer.getTimeLeft() < 0:
            self.stop()
            
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
        self.rowan.char.hit(self.enemy)
        self.enemy.char.hit(self.rowan)
        keepGoing = True
        while keepGoing:
            if self.enemy.char.hitPoints <= 0:
                self.enemies.remove(self.enemy.char)
                keepGoing = False
            elif self.rowan.char.hitPoints <= 0:
                self.rowan.char.hitPoints = 0
                game.stop()
                keepGoing = False
            else:
                self.enemy.char.hit(self.rowan)
                self.rowan.char.hit(self.enemy)
            print(f"""Enemy: {self.enemy.char.hitPoints}
Rowan: {self.rowan.char.hitPoints}""")
#                 self.hitPoints = self.rowan.char.hitPoints

        self.lblHP.text = f"HP: {self.rowan.char.hitPoints}"
                
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("instructionsScroll.png")
        
        self.response = "Deny"
        
        self.instructions = simpleGE.MultiLabel()
        self.bgColor = "white"
        self.fgColor = "black"
        self.instructions.textLines = ["Well met, Traveler! You are Rowan the Swift. Your mission,",
                                       "should you choose to accept it, is to find the magical healing",
                                       "elixir in the city of Camelot. It's imperative that you are",
                                       "quick about it because the princess's life is at stake.",
                                       "Along the way, you will have the opportunity to pick up",
                                       "healing potions to boost your health stats",
                                       "",
                                       "Press <SPACE> to fight.",
                                       "To win, you must get the elixir to the King within 10 minutes.",
                                       "Do try not to die.",
                                       ]
        self.instructions.center = (320, 200)
        self.instructions.size = (600, 300)
#         self.instructions.font = pygame.font.match_font("vinerITC")
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Accept (up)"
        self.btnPlay.center = (100, 400)
        self.btnPlay.bgColor = "white"
        self.btnPlay.fgColor = "black"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Deny (down)"
        self.btnQuit.center = (550, 400)
        self.btnQuit.bgColor = "white"
        self.btnQuit.fgColor = "black"
        
        self.sprites = [self.instructions,
                        self.btnPlay,
                        self.btnQuit]
    def process(self):
        if self.btnQuit.clicked:
            self.response = "Deny"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Accept"
            self.stop()
        if self.isKeyPressed(pygame.K_UP):
            self.response = "Accept"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.response = "Deny"
            self.stop()
    
def main():
    keepGoing = True
    while keepGoing:
        instructions = Instructions()
        instructions.start()
        
        if instructions.response == "Accept":
            game = Game()
            game.start()
            
        else:
            instructions.stop()
            keepGoing = False
    game.stop()
    
if __name__ == "__main__":
    main()
