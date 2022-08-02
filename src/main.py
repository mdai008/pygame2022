from sprites import * 

#game class
class game:
    def __init__(self): 
        pg.init() 
        self._screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
        self._clock = pg.time.Clock() 
        # self._font = pg.font.Font("Arial", 32) 
        self.isRunning = True 

        # self.characterSheet = spriteSheet("sheetLoc") 
        # self.terrainSheet = spriteSheet("sheetLoc")
        # self.enemySheet = spriteSheet("sheetLoc")  
        # self.attackSheet = spriteSheet("sheetLoc")

    def createMap(self): #create tile map 
        for i, row in enumerate(tileMap): 
            for j, column in enumerate(row): 
                ground(self, j, i)
                if column == "X": 
                    wall(self, j, i) 
                if column == "P": 
                    self.player = player(self, j, i) 
                if column == "E": 
                    enemy(self, j, i) 
                # if column == "D": 
                #     destructibleWall(self, j, i) 

    def newGame(self): #initializes variables when game starts
        self._isPlaying = True 
        self.allSprites = pg.sprite.LayeredUpdates() 
        self.walls = pg.sprite.LayeredUpdates() 
        self.destructibleWalls = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.LayeredUpdates() 
        self.attacks = pg.sprite.LayeredUpdates() 
        self.players = pg.sprite.LayeredUpdates()
        self.createMap() 

    def events(self): #key inputs
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                self._isPlaying = False
                self.isRunning = False
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_SPACE: 
                    xPos = self.player.rect.x + (TILE_SIZE / 2) - (ATTACK_SIZE / 2) 
                    yPos = self.player.rect.y + (TILE_SIZE / 2) - (ATTACK_SIZE / 2) 
                    playerAttack(self, xPos, yPos)
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_r: 
                    g.newGame()
                    g.main()

    def update(self): #update game variables
        self.allSprites.update() 

    def draw(self): #display sprites
        self._screen.fill(BLACK) 
        self.allSprites.draw(self._screen) 
        self._clock.tick(FPS) 
        pg.display.update() 
    
    def main(self): 
        while self._isPlaying:
            self.events()
            self.update()
            self.draw()

        self.isRunning = False 
    
    def gameOver(self):
        pass

    def introScreen(self):
        pass


#main program
g = game() 
g.introScreen() 
g.newGame() 

while g.isRunning: 
    g.main()
    g.gameOver()

pg.quit() 
sys.exit() 