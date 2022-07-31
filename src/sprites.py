import pygame as pg
import sys
import math
import random

#variables
WIN_WIDTH, WIN_HEIGHT = 800, 672 
TILE_SIZE = 32 
FPS = 60
PLAYER_LAYER = 4 
ENEMY_LAYER = 3
WALL_LAYER = 2
GROUND_LAYER = 1
PLAYER_SPEED = 2
ENEMY_SPEED = 1 
MOVEMENT_INC = 1
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GRAY = (127, 127, 127)

# class spriteSheet: #class for a sprite sheet
#     def __init__(self, file):
#         self._sheet = pg.image.load(file).convert() 

#     def getSprite(self, x, y, width, height): 
#         sprite = pg.Surface([width, height]) 
#         sprite.set_colorkey(BLACK) 
#         sprite.blit(self._sheet, (0,0), (x, y, width, height)) 
#         return sprite

#player class
class player(pg.sprite.Sprite): 
    def __init__ (self, g, x, y):
        self._game = g 
        self._layer = PLAYER_LAYER 
        self._groups = self._game.allSprites 
        pg.sprite.Sprite.__init__(self, self._groups)

        self._width = TILE_SIZE 
        self._height = TILE_SIZE 
        self._x = x * TILE_SIZE 
        self._y = y * TILE_SIZE 

        self.image = pg.Surface([self._width, self._height]) 
        self.image.fill(BLUE) 
        # self.image = self._game.characterSheet.getSprite(x, y, self._width, self._height)
        
        self.rect = self.image.get_rect() 
        self.rect.x = self._x 
        self.rect.y = self._y 

        self._xChange = 0 
        self._yChange = 0 
        self._facing = "down" 
        # self._animationDict = {
        # "leftAni": [self._game.characterSheet.getSprite(x, y, self._width, self._height), ],
        # "rightAni": [self._game.characterSheet.getSprite(x, y, self._width, self._height), ],
        # "upAni": [self._game.characterSheet.getSprite(x, y, self._width, self._height), ],
        # "downAni": [self._game.characterSheet.getSprite(x, y, self._width, self._height), ]
        # }
        # self._animationLoop = 1 

    def update(self): #update character position
        self.movement() 
        # self.animateSprite() 
        self.rect.x += self._xChange 
        self.wallCollision("x")
        self.rect.y += self._yChange
        self.wallCollision("y") 
        self._xChange = 0 
        self._yChange = 0 
        
    def movement(self): #player movement
        keys = pg.key.get_pressed() 
        if keys[pg.K_a]: 
            for sprite in self._game.allSprites: 
                sprite.rect.x += PLAYER_SPEED
            self._xChange -= PLAYER_SPEED 
            self._facing = "left" 
        if keys[pg.K_d]: 
            for sprite in self._game.allSprites: 
                sprite.rect.x -= PLAYER_SPEED
            self._xChange += PLAYER_SPEED 
            self._facing = "right" 
        if keys[pg.K_w]: 
            for sprite in self._game.allSprites: 
                sprite.rect.y += PLAYER_SPEED
            self._yChange -= PLAYER_SPEED 
            self._facing = "up" 
        if keys[pg.K_s]: 
            for sprite in self._game.allSprites: 
                sprite.rect.y -= PLAYER_SPEED
            self._yChange += PLAYER_SPEED 
            self._facing = "down" 

    def wallCollision(self, direction): #collision detection
        if direction == "x": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._xChange > 0: 
                    self.rect.x = isHit[0].rect.left - self.rect.width 
                    for sprite in self._game.allSprites: 
                        sprite.rect.x += PLAYER_SPEED
                if self._xChange < 0: 
                    self.rect.x = isHit[0].rect.right 
                    for sprite in self._game.allSprites: 
                        sprite.rect.x -= PLAYER_SPEED
        if direction == "y": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._yChange > 0: 
                    self.rect.y = isHit[0].rect.top - self.rect.height 
                    for sprite in self._game.allSprites: 
                        sprite.rect.y += PLAYER_SPEED
                if self._yChange < 0: 
                    self.rect.y = isHit[0].rect.bottom 
                    for sprite in self._game.allSprites: 
                        sprite.rect.y -= PLAYER_SPEED

    # def animateSprite(self): #animate sprite
    #     leftAni = [self._game.characterSheet.getSprite(x, y, self._width, self._height)] 
    #     rightAni = [self._game.characterSheet.getSprite(x, y, self._width, self._height)] 
    #     upAni = [self._game.characterSheet.getSprite(x, y, self._width, self._height)] 
    #     downAni = [self._game.characterSheet.getSprite(x, y, self._width, self._height)] 
    #     if self._facing == "left":
    #         if self._xChange == 0: 
    #             self.image = leftAni[0] 
    #         else: 
    #             self.image = leftAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "right":
    #         if self._xChange == 0: 
    #             self.image = rightAni[0] 
    #         else: 
    #             self.image = rightAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "up":
    #         if self._yChange == 0: 
    #             self.image = upAni[0] 
    #         else: 
    #             self.image = upAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "down":
    #         if self._yChange == 0: 
    #             self.image = downAni[0] 
    #         else: 
    #             self.image = downAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1

#enemy class
class enemy(pg.sprite.Sprite): 
    def __init__(self, g, x, y):
        self._game = g 
        self._layer = ENEMY_LAYER 
        self._groups = self._game.allSprites, self._game.enemies 
        pg.sprite.Sprite.__init__(self, self._groups) 

        self._width = TILE_SIZE 
        self._height = TILE_SIZE 
        self._x = x * TILE_SIZE 
        self._y = y * TILE_SIZE 

        self.image = pg.Surface([self._width, self._height])
        self.image.fill(RED) 
        # self.image = self._game.enemySheet.getSprite(x, y, width, height) 

        self.rect = self.image.get_rect() 
        self.rect.x = self._x 
        self.rect.y = self._y 

        self._xChange = 0 
        self._yChange = 0 
        self._facing = random.choice(["left", "right", "up", "down"]) 
        self._movementLoop = 0 
        self._maxDist = random.randint(10,20) 
        # self._animationDict = {
        # "leftAni": [self._game.enemySheet.getSprite(x, y, self._width, self._height), ],
        # "rightAni": [self._game.enemySheet.getSprite(x, y, self._width, self._height), ],
        # "upAni": [self._game.enemySheet.getSprite(x, y, self._width, self._height), ],
        # "downAni": [self._game.enemySheet.getSprite(x, y, self._width, self._height), ]
        # }
        # self._animationLoop = 1 

    def update(self): #update enemy position
        self.movement() 
        # self.animateSprite() 
        self.rect.x += self._xChange 
        self.wallCollision("x") 
        self.rect.y += self._yChange 
        self.wallCollision("y") 
        self._xChange = 0 
        self._yChange = 0 

    def movement(self): #how the enemy moves
        if self._facing == "left": 
            self._xChange -= ENEMY_SPEED
            self._movementLoop -= MOVEMENT_INC 
            if self._movementLoop <= -self._maxDist: 
                self._facing = random.choice(["left", "right", "up", "down"]) 
        if self._facing == "right": 
            self._xChange += ENEMY_SPEED
            self._movementLoop += MOVEMENT_INC 
            if self._movementLoop >= self._maxDist: 
                self._facing = random.choice(["left", "right", "up", "down"]) 
        if self._facing == "up": 
            self._yChange -= ENEMY_SPEED
            self._movementLoop -= MOVEMENT_INC 
            if self._movementLoop <= -self._maxDist: 
                self._facing = random.choice(["left", "right", "up", "down"]) 
        if self._facing == "down": 
            self._yChange += ENEMY_SPEED
            self._movementLoop += MOVEMENT_INC 
            if self._movementLoop >= self._maxDist: 
                self._facing = random.choice(["left", "right", "up", "down"]) 

    def wallCollision(self, direction): #collision detection
        if direction == "x": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._xChange > 0: 
                    self.rect.x = isHit[0].rect.left - self.rect.width 
                    self._facing = random.choice(["left", "up", "down"]) 
                if self._xChange < 0: 
                    self.rect.x = isHit[0].rect.right 
                    self._facing = random.choice(["right", "up", "down"]) 
        if direction == "y": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._yChange > 0: 
                    self.rect.y = isHit[0].rect.top - self.rect.height 
                    self._facing = random.choice(["left", "right", "up"]) 
                if self._yChange < 0: 
                    self.rect.y = isHit[0].rect.bottom 
                    self._facing = random.choice(["left", "right", "down"]) 

    # def animateSprite(self): #animate sprite
    #     leftAni = [self._game.enemySheet.getSprite(x, y, self._width, self._height)] 
    #     rightAni = [self._game.enemySheet.getSprite(x, y, self._width, self._height)] 
    #     upAni = [self._game.enemySheet.getSprite(x, y, self._width, self._height)] 
    #     downAni = [self._game.enemySheet.getSprite(x, y, self._width, self._height)] 
    #     if self._facing == "left":
    #         if self._xChange == 0: 
    #             self.image = leftAni[0] 
    #         else: 
    #             self.image = leftAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "right":
    #         if self._xChange == 0: 
    #             self.image = rightAni[0] 
    #         else: 
    #             self.image = rightAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "up":
    #         if self._yChange == 0: 
    #             self.image = upAni[0] 
    #         else: 
    #             self.image = upAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1
    #     if self._facing == "down":
    #         if self._yChange == 0: 
    #             self.image = downAni[0] 
    #         else: 
    #             self.image = downAni[math.floor(self._animationLoop)] 
    #             self._animationLoop += 0.1 
    #             if self._animationLoop >= 3: 
    #                 self._animationLoop = 1

#wall class
class wall(pg.sprite.Sprite): 
    def __init__(self, g, x, y):
        self._game = g 
        self._layer = WALL_LAYER 
        self._groups = self._game.allSprites, self._game.walls 
        pg.sprite.Sprite.__init__(self, self._groups) 

        self._width = TILE_SIZE 
        self._height = TILE_SIZE 
        self._x = x * TILE_SIZE 
        self._y = y * TILE_SIZE 

        self.image = pg.Surface([self._width, self._height]) 
        self.image.fill(GREEN) 
        # self.image = self._game.terrainSheet.getSprite(x, y, width, height)

        self.rect = self.image.get_rect() 
        self.rect.x = self._x 
        self.rect.y = self._y 

#ground class
class ground(pg.sprite.Sprite): 
    def __init__(self, g, x, y):
        self._game = g 
        self._layer = GROUND_LAYER 
        self._groups = self._game.allSprites 
        pg.sprite.Sprite.__init__(self, self._groups) 

        self._width = TILE_SIZE 
        self._height = TILE_SIZE 
        self._x = x * TILE_SIZE 
        self._y = y * TILE_SIZE 

        self.image = pg.Surface([self._width, self._height]) 
        self.image.fill(GRAY) 
        # self.image = self._game.terrainSheet.getSprite(x, y, width, height) 

        self.rect = self.image.get_rect() 
        self.rect.x = self._x 
        self.rect.y = self._y 








#map boundaries
tileMap = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X................................................X",    
    "X..E.........X...........................E.......X",
    "X............X...................X.X.............X",
    "X....XXXX....X..................X....XX.....XXX..X",
    "X....X..........................X.E..X.....X..X..X",
    "X....X.....X.....................XXX..X...X...X..X",
    "X....X.E...X.......................X..X..X....X..X",
    "X....XXXXXXX..........X............X..X..X....X..X",
    "X...................................E.X..X.E..X..X",
    "X...........P.......X...X..........XXX...........X",
    "X.......X..............E.........................X",
    "X........X............X..........................X",
    "X.........X...........................XXX........XXXXXXXXXXXXXXXXXXXXX",
    "X...........XXXXX.....E..............................................X",
    "X.....E.......................X............E.........................XX",
    "X..........X..E...............X........................................XX",
    "X..........X..................X........E.................................X",
    "X..........X......E...........X...........................................XXX",
    "X............................................................................X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
] 

