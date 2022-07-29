import pygame as pg
import sys
import math
import random

#variables
WIN_WIDTH, WIN_HEIGHT = 800, 640 
TILE_SIZE = 32 
FPS = 60
PLAYER_LAYER = 3 
WALL_LAYER = 2
GROUND_LAYER = 1
PLAYER_SPEED = 3
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

    def update(self): #update character position
        self.movement() 
        self.rect.x += self._xChange 
        self.wallCollision("x")
        self.rect.y += self._yChange
        self.wallCollision("y") 
        self._xChange = 0 
        self._yChange = 0 
        
    def movement(self): #player movement
        keys = pg.key.get_pressed() 
        if keys[pg.K_a]: 
            self._xChange -= PLAYER_SPEED 
            self._facing = "left" 
        if keys[pg.K_d]: 
            self._xChange += PLAYER_SPEED 
            self._facing = "right" 
        if keys[pg.K_w]: 
            self._yChange -= PLAYER_SPEED 
            self._facing = "up" 
        if keys[pg.K_s]: 
            self._yChange += PLAYER_SPEED 
            self._facing = "down" 

    def wallCollision(self, direction): #collision detection
        if direction == "x": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._xChange > 0: 
                    self.rect.x = isHit[0].rect.left - self.rect.width 
                if self._xChange < 0: 
                    self.rect.x = isHit[0].rect.right 
        if direction == "y": 
            isHit = pg.sprite.spritecollide(self, self._game.walls, False) 
            if isHit: 
                if self._yChange > 0: 
                    self.rect.y = isHit[0].rect.top - self.rect.height 
                if self._yChange < 0: 
                    self.rect.y = isHit[0].rect.bottom 

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
    "X..P.............................................X",
    "X................................................X",
    "X....XXXX........................................X",
    "X................................................X",
    "X..........X.....................................X",
    "X..........X.....................................X",
    "X..........X.....................................X",
    "X................................................X",
    "X................................................X",
    "X................................................X",
    "X................................................X",
    "X................................................X",
    "X...........XXXXX................................X",
    "X................................................X",
    "X................................................X",
    "X................................................X",
    "X................................................X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
] 

