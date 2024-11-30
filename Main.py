import Module1
import os
import sys
from time import sleep
import time
timer = 100

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Player: 
    def __init__(self):
        self.Health=100
        self.Gold=0
        self.Level=1
        self.playerX= 0
        self.playerY= 0
        self.isDead=False
        self.hasChecked =False
    def collisionCheck(self,space,direction,x,y):

        if(space == "E"):
            gameboard.board[x][y] = 0
            self.Health = self.Health - 15
            self.Gold = self.Gold + 15
            self.hasChecked = True
           
            self.move(direction)
			#if player hits enemy, player loses health
        elif(space == "+"):
            self.Health = self.Health + 20
            gameboard.board[x][y] = 0
            self.hasChecked = True
            self.move(direction)
            #if player hits heal, player heals health
        elif(space == "?"):
            self.Health = self.Health * 2
            gameboard.board[x][y] = 0
            self.hasChecked = True
            self.move(direction)
            #if player hits easter egg, player doubles health
        elif(space == "O"):
            for i in range(0,len(gameboard.board)):
                for j in range(0,len(gameboard.board)):
                    if(gameboard.board[i][j] == "E"):
                        gameboard.board[i][j] = 0
                        self.Gold = self.Gold + 15
            #if player hits fireball, all enemies on screen are killed
	
            gameboard.board[x][y] = 0
            self.hasChecked = True
            self.move(direction)
        elif(space == 0):

            self.hasChecked = True
        else:
            if(self.Gold > 100):
                self.Level = self.Level + 1
		self.Gold = self.Gold - 100
                gameboard.height = gameboard.height + 1
                gameboard.width = gameboard.width + 1
                gameboard.board = [[0 for i in range(gameboard.width)] for j in range(gameboard.height)]
                gameboard.randomizeBoard()
                global timer
                timer = round(100*0.95**self.Level)
                
                self.hasChecked = False
                
            else:
                print("Not enough gold!")

    def move(self,direction):

            if(direction == "up"):
                try:
                    if(self.hasChecked == False):
                        self.collisionCheck(gameboard.board[self.playerX - 1][self.playerY],"up",self.playerX-1,self.playerY)
                        
                except:
                    pass
                
                if(self.hasChecked == True):
                    gameboard.board[self.playerX][self.playerY] = 0

                    self.playerX = self.playerX - 1
                    try:
                        gameboard.board[self.playerX][self.playerY] = "^"
                    except:
                        
                        self.playerX = self.playerX + 1  
                        gameboard.board[self.playerX][self.playerY] = "^"
                    self.hasChecked = False
                    refresh()
                    
                    
                
    
			
            if(direction == "down"):
                
                if(self.hasChecked == False):
                    try:
                        self.collisionCheck(gameboard.board[self.playerX + 1][self.playerY],"down",self.playerX+1,self.playerY)
                       
                    except:
                        pass

                    
                if(self.hasChecked == True):
                    gameboard.board[self.playerX][self.playerY] = 0
                    self.playerX = self.playerX + 1
                    try:
                        gameboard.board[self.playerX][self.playerY] = "^"
                    except:
                    
                        self.playerX = self.playerX - 1  
                        gameboard.board[self.playerX][self.playerY] = "^"
                      
                    self.hasChecked = False
                    refresh()
                    
                
            if(direction=="left"):
                try:
                    if(self.hasChecked == False):
                        self.collisionCheck(gameboard.board[self.playerX][self.playerY-1],"left",self.playerX,self.playerY-1)
                except:
                    pass
			
                if(self.hasChecked == True):
                    gameboard.board[self.playerX][self.playerY] = 0
                    self.playerY = self.playerY -1
                    try:
                        gameboard.board[self.playerX][self.playerY] = "^"
                    except:
                        
                        self.playerY = self.playerY + 1  
                        gameboard.board[self.playerX][self.playerY] = "^"
                      
                    self.hasChecked = False
                    
                    refresh()
                
                

            if(direction== "right"):
                try:
                    if(self.hasChecked == False):
                        self.collisionCheck(gameboard.board[self.playerX][self.playerY+1],"right",self.playerX,self.playerY+1)
                except: pass
                if(self.hasChecked == True):
                    gameboard.board[self.playerX][self.playerY] = 0
                    self.playerY = self.playerY  + 1
                    try:
                    
                        gameboard.board[self.playerX][self.playerY] = "^"
                    except:
                
                        self.playerY = self.playerY - 1  
                        gameboard.board[self.playerX][self.playerY] = "^"
                    self.hasChecked = False
                    refresh()
            








import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.keypad(True)
gameboard = Module1.Board(10,10,100)
gameboard.randomizeBoard()
startTime = time.time()
player = Player()
gameboard.board[player.playerX][player.playerY] = "^"

for rows in gameboard.board:
    
    print("\n",rows,end="")
print("\nThis is your board. The elements are:\n 0: Empty walking space\n ^: This is your player\nE: The enemy, run into it for some gold\n +: A heal, run into it for a heal\n ?: Doubles your health, but incredibly rare\n O: Kills every enemy on the map and gives you their gold\n$: This is the goal. Touch it with 100 gold to buy entrance to the next level\n Use WASD to move. Move to begin playing. You have a limited amount of moves per level, and it decreases with level, so be careful!")
def refresh():
    
    for rows in gameboard.board:
    
        print("\n",rows,end="") 
    print("\nYou have",player.Health,"health.", "You have ",player.Gold," gold. ","You are at level ",player.Level,". You are at ", "(",player.playerX,",",player.playerY,")",end="")

    print(" You have",timer,"moves left.")
    



    
while player.isDead == False:
    timer = timer - 1
    if(timer == 0):
        print("Ran out of moves, rerun the program!")
        player.isDead = True
        sleep(1000)
     
    c = stdscr.getch()
    
    if(player.Health == 0):
        print("You died, rerun the program.")
        player.isDead = True
        sleep(1000)
    if c == ord('a'):
        if(player.playerY != 0):
            
            player.move('left')
       
    elif c == ord('s'):

        player.move('down')
        
        
    elif c == ord('d'):
        
        player.move('right')
        
    elif c == ord('w'):
        if(player.playerX != 0): 
            player.move('up')
