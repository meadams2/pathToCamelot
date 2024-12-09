# The Path to Camelot

Well met, Traveler! You are Rowan the Swift. Your mission, should you choose to accept it, is to find the magical healing elixir in the city of Camelot. It's imperative that you are quick about it because the princess's life is at stake. Along the way, you will have the opportunity to pick up healing potions to boost your health stats. Various scoundrels and thieves from Avalon will try to thwart you, but you mustn't let them. 

To win, you must get the elixir to the King within a 10 minute time frame with at least 10 HP. Do try not to die, young knight.

## Where I got Stuck

I had issues getting the potions to work how I wanted, so I ended up ignoring the potions for the time being. Additionally, I ran into issues with the fight class. I also had issues getting a different font to work. 

Potentially in the future, I would play around with a second game file called "pathToCamelot.py" that would ignore multiple inheritances. 

## Game Design Images

### Intro Screen

Very rough sketch of what the instructions screen will look like. Instructions have changed with further planning.

![Instructions Screen](https://github.com/meadams2/pathToCamelot/blob/main/Game%20Dev/PathtoCamelotInstructions.jpg)

### Gameplay

Very rough sketch of what the gameplay will look like. Tilebased world. 

![Gameplay Screen](https://github.com/meadams2/pathToCamelot/blob/main/Game%20Dev/PathtoCamelotGameplay.jpg)

## Assets 

- Instructions Screen Scroll Background from https://openclipart.org/detail/271009/scroll-2 by Arvin61r58
  
### Tile Textures

-	Grass, Path, Forest, and Water created by Ian Voiral under CC-BY 3.0, GPL 3.0, GPL 2.0. Link to Site: https://opengameart.org/content/basic-map-32x32-by-ivan-voirol

### Sprites 

- Rowan—Character sheet created using https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/#?body=Body_color_light&head=Human_male_light.
- Bosses and Monsters Spritesheets—Created by Stephen Challener (Redshrike) under CC-BY3.0. Link: https://opengameart.org/content/bosses-and-monsters-spritesheets-ars-notoria.
- Potions—Created by Hyptosis and Zabin under CC-BY 3.0. Link to site: https://opengameart.org/content/lots-of-free-2d-tiles-and-sprites-by-hyptosis.
- 98 Pixel Art RPG Icons—Created by 7Soul under CC-BY 3.0. Link to site: https://opengameart.org/content/98-pixel-art-rpg-icons.
  - Used for Elixir

## Milestones

### Overall Idea Scheme

1. Scene
2. Characters
3. Objects
4. Walls
5. Labels and buttons
6. Instructions screen
7. Win screen

### Timeline

- 11/19 Basic scene with basic characters
- 11/22 Objects
- 11/25 Walls
- 12/2 Labels and Buttons
- 12/5 Instructions screen
- 12/9 Walls

### Stretch Goals
- Save and load functionality
- Levels

## Psuedocode

Main things I want in the game:

- Method to check if the character is within bounds of current tile
- Method to "pick up" objects
- Check if arrow keys, "a", or <SPACE> pressed
- How do attacks occur?
- Walls (ie, places characters can't walk)
- Win screen
- Varying difficulties with the enemies

### Character Module

Will be in module separate from gameplay. Defines what a "character" is. Can either be defining an enemy or Rowan the Swift.

Attributes:
- Name
- hitPoints 
  - Indicates the health status of the character
  - In terms of coding, it defines how much more damage the character can take
  - HP can go negative
- maxDamage
  - Indicates the maximum damage a character can deal to their opponent
  - maxDamage is greater than 0
  - maxDamage will not be the damage the character does everytime 
- hitChance
  - Indicates how likely the character is to hit the opponent
  - Is a percent
  - Integer between 1-100
- healingFactor
  - Indicates how likely the character is to heal between "hits"
  - Is a percent
  - Integer between 1-100
- maxHealing
  - Maximum amount a character can heal between hits
  - Greater than 0
  - maxHealing will not be the amount the character heals everytime
- armor
  - Does the character have any protection
  - Integer between 0 and 10

#### Initializing

Sets image for characters. Sets position and how the character moves within the game scheme. 

Calls the attributes and assigns them to be public. Defines dx and dy, should move 3 pixels per frame. 

#### Hit Method

Takes self and enemy. Generate a random number between 1-100. If number is less than or equal to hitChance, hit lands. After hit, generate damage using random integer between 1 and maxDamage. Subtract enemy armor from hit damage.

Generate random number between 1-100. If number is less than or equal to healingFactor, character heals. Generate healing using random integer between 1 and maxHealing. Subtract from hit damage. 

Subtract hitDamage from enemy hitPoints. Return enemy hitPoints. 

### Rowan Class

Initializes name and health stats of Rowan. Add image. Uses Character Module.

Initialize inventory. Inventory gets empty list. 

#### Process Method 

##### Standard Motion
If left arrow key pressed, character moves in negative x direction. If right arrow key pressed, character moves in positive x direction. 

If up arrow key pressed, character moves in negative y direction. If down arrow key pressed, character moves in positive y direction.

If space bar is pressed, check if character collideswith an enemy. If so, call fight method. 

If "a" pressed, check if character collideswith an object. If so, call pickUp method. 

If "d" pressed, check if healing potion in inventory. If so, call heal method. 

##### Adjust Movement Speed by Terrain 

If tileState is 0, movespeed gets 2. If tileState is 1, movespeed gets 5. If tileState is 2, movespeed gets 0.5. If tileState is 3, movespeed is 0.2. 

#### Fight Method

For loop. Each time <SPACE> pressed, character1 hits character2 and character 2 hits character1. Get hitPoints. If hitPoints less than or equal to 0, character dies. Else, check for key press.

#### Pick Up Method

Append object to inventory list. 

#### Heal Method

Remove object from inventory and get healthAdd from object class. Add healthAdd to HP. 

### Enemy Class

Inherits from Character module. Randomize HP, healingFactor, hitChance, armor, and maxDamage. Sets image from list of enemy images.

### Potions Class

Calls simpleGE.sprite. Sets image. Sets position. Position will be random in game scheme. Sets healthAdd. healthAdd will be random integer from 0-5. 

### Elixir Class

Calls simpleGE.sprite. Sets image. Sets position. 

### Tile Class

Will be a tile based map. Plan will be shown in CSV file. Initialize list of images for tiles. Tile size is (32, 32). 

- Grass marked in map as 0
- The path marked as 1
- Water marked as 2
- Forest marked as 3
  
Default state is Grass.

#### Setting the State

Copy the image corresponding with the state. 

### Labels

Define new class called LblHP that takes simpleGE.Label. LblHP will be label with hitPoints. Label text should say "HP: 0" as the default. Center at (100, 30). Set label color to "white". Set label font to "Vinter Hand ITC". 

Define new class called LblTime. LblTime takes simpleGE.Label. LblTime will be label with time. Time gets lblTime / 60 to get time in minutes. Label text should say "Time Left: 10 minutes". Set label color to "white". Set label font to "Vinter Hand ITC". 

### Game Class

Defines what the game behavior is. 

#### Initializing

Initialize simpleGE.scene. 

Initialize tileset. Tileset is empty list. Make constant defining rows. There will be 20 rows. Make constant defining the columns. There will be 40 columns. 

Define how many rows of the map will be on screen at once using constant. There will be 5 rows depicted at a time. Make constant defining the columns on a screen at a time. There will be 10 columns shown at a time. Define off row as 0. Define off column as 0. 

Add tileset to list of sprites. 

Initialize timing. 

Call Rowan class. Assume default behavior. Add to list of sprites. 

Create empty list under "enemies". For loop, range 8. Call Enemy class. Assume default behavior. Add to list of enemies. Add to list of sprites. 

Create empty list under "potions". For loop, range 10. Call Potions class. Default behavior. Add to list of potions. Add potions to list of sprites. 

Call Elixir class. Assume default behavior. Add to list of sprites. 

Call labels. Add to list of sprites. 

#### Load Map Method

Make state system defining where each tile is in memory. Each tile will be 0, 1, 2, or 3. For each row in range of screen rows constant, append [] to the tileset. For each column, create a new tile and set the state. Set the x position to 16 + (32 * column). Set the y position to 16 + (32 * row). Tile x position gets the x position. Tile y position gets the y position. Append to the tileset row. 

#### Show Map Method

Shows a subset of the map. Subset is the screen rows and screen columns. For each row, and for each column, the current value is the self.map of the row + self.offRow times the column +self.offColum. Use to set the tileset state. 

#### Process Method

Check if left key pressed. Then check if self.offCol is greater than 0. If so, offCol gets subtracted by 1. 

Check if right key is pressed. Then check if self.offCol is less than the difference between the total columns and the screen columns. If so, add 1 to offCol. 

Check if up key is pressed. Then check if self.offRow is greater than 0. If so, subtract 1 from offRow. 

Check if down key is pressed. Then check if self.offRow is less than the difference between total number of rows and the screen rows. If so, add 1 to offRow. 

Update lblTime text. Each frame, check if Elixir in inventory, if so, win. If time left is less than 0, check if Elixir in Rowan.inventory. If so, win screen. Else, lose. 

Call showMap(). 

### Instructions

Define new class called Instructions that takes simpleGE.Scene. 

#### Label
Define initializing method. Init method takes self. Set background image to instructionsScroll.png. 

Set MultiLabel background color to white. Set font to "Viner Hand ITC". Instructions text will read: 

> Well met, Traveler! You are Rowan the Swift. Your mission, should you choose to accept it, is to find the magical healing elixir in the city of Camelot. It's imperative that you are quick about it because the princess's life is at stake. Along the way, you will have the opportunity to pick up healing potions to boost your health stats. Various scoundrels and thieves from Avalon will try to thwart you, but you mustn't let them.
> 
>To win, you must get the elixir to the King within a 10 minute time frame with at least 10 HP. Do try not to die, young knight.
> 
> Use the arrow keys to move, press <SPACE> to attack, press "a" to pick up an object. Press "d" to use an object.

Center instructions at (320, 240). Scale instructions to (500, 250). 

Add self.instructions to list of sprites. 

#### Buttons

Buttons should do the respective action when clicked or the corresponding key is pressed. 

Initialize simpleGE.Button() and store in self.btnPlay. Play button should read "Play (up)". Center at (100, 400). Change label color to white. Set font to "Viner Hand ITC". Add self.btnPlay to list of sprites. 

Initialize simpleGE.Button() and store in self.btnQuit. Quit button should read "Quit (down)". Center at (550, 400). Change label color to white. Set font to "Viner Hand ITC". Add self.btnQuit to list of sprites. 

#### Process Method

If play button is clicked, response gets "Play" and instructions scene stops. If up arrow key is pressed, response gets "Play" and instruction scene stops. 

If quit button is clicked, response gets "Quit" and instruction scene stops. If down arrow key is pressed, response gets "Quit" and instruction scene stops. 

### Win

Define initializing method. Win will use simpleGE.Scene. Set background image to "instructionsScroll.png". Use multilabel and store in self.win. Textbox should read:
> Congratulations, young knight! Thank you for saving my daughter.

Set label color to white. Set font to "Vinter Hand ITC". Center at (320, 240). Set size to (500, 250). 

Create "Play Again" button with simpleGE.button(). Button should read "Play Again (up)". Label color should be white. Set font to "Vinter Hand ITC". Center at (100, 400). Create "Quit" button with simpleGE.button(). Button should read "Quit (down)". Center at (550, 400). 

Add to list of sprites. 

#### Process Method

If play again button clicked, response gets play again. Check for up key press. Response gets play again. 

If quit button clicked, response gets Quit. Check for down key press. Response gets quit. 

### Lose 

Define initializing method. Lose will use simpleGE.Scene. Set background image to "InstructionsScroll.png". Use multilabel and store in self.lose. Textbox should read:
> You didn't get the Elixir in time. As a result, the princess has died and war has started with Avalon.

Set label color to white. Set font to "Vinter Hand ITC". Center at (320, 240). Set size to (500, 250). 

Create "Play Again" button with simpleGE.button(). Button should read "Play Again (up)". Label color should be white. Set font to "Vinter Hand ITC". Center at (100, 400). Create "Quit" button with simpleGE.button(). Button should read "Quit (down)". Center at (550, 400). 

Add to list of sprites. 

#### Process Method

If play again button clicked, response gets play again. Check for up key press. Response gets play again. 

If quit button clicked, response gets Quit. Check for down key press. Response gets quit. 

### Main Function

Call instructions. If instructions.response is "Play", start the game. If instructions.response is "Quit", stop the instructions. 

Initialize while loop with keepGoing = True sentry. 

If game.level is "Win", win.start(). If win.response is "Quit", keepGoing gets false. If response is "Play Again", start game. 

If game.level is "lose", lose.start(). If lose.response is "Quit", keepGoing gets false. If response is "Play again", start game. 
