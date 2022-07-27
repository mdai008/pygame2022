import pygame as pg
import sys
import math
import random

#variables
WIN_WIDTH, WIN_HEIGHT = 800, 640 
TILE_SIZE = 32 
FPS = 60
PLAYER_LAYER = 2 
WALL_LAYER = 1
PLAYER_SPEED = 3
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 


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
        
        self.rect = self.image.get_rect() 
        self.rect.x = self._x 
        self.rect.y = self._y 

        self._xChange = 0 
        self._yChange = 0 
        self._facing = "down" 

    def update(self): #update character position
        self.movement() 
        self.rect.x += self._xChange 
        self.rect.y += self._yChange 
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

