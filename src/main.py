from sprites import * 

#game class
class game:
    def __init__(self): 
        pg.init() 
        self._screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) 
        self._clock = pg.time.Clock() 
        # self._font = pg.font.Font("Arial", 32) 
        self.isRunning = True 

    def newGame(self): #initializes variables when game starts
        self._isPlaying = True 
        self.allSprites = pg.sprite.LayeredUpdates() 
        self._walls = pg.sprite.LayeredUpdates() 
        self._enemies = pg.sprite.LayeredUpdates() 
        self._attacks = pg.sprite.LayeredUpdates() 
        self._player = player(self, 1, 2) 

    def events(self): #key inputs
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                self._isPlaying = False
                self.isRunning = False

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