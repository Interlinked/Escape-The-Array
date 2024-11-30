
import random
import time
from time import sleep
timer = 100
class Board:
    def __init__(self, width, height,timer):
        self.height = height
        self.width = width
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]
        self.timer = timer
        #creates a 2d array by making a list of lists
    def randomizeBoard(self):
        
        enemyCount = 8
        goalHasPlaced = False
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board)):
                #iterates over the number of rows, then the number of elements within each row
                #hits every element
                chance = random.randint(0,100)
                if(self.board[i][j] == 0):
                #only randomizes an element if it isn't already randomized
                    #0.25% chance to spawn a fireball
                    if(chance <= 1):
                        if(random.randint(0,20) >= 10):
                            #checks for a 1% chance, then a 25% percent chance to get a 0.25% chance
                            self.board[i][j] = "O"
                    if(enemyCount > 0):
                        #10% chance to spawn an enemy
                        if(chance <= 15 and chance > 5):
                            self.board[i][j] = "E"
                    
                            enemyCount -= 1
                    #checks if the board has the maximum amount of enemies
                    #10% chance to spawn a heal
                    if(chance <= 25 and chance > 15):
                        self.board[i][j] = "+"
                    #checks if a goal has been placed, if not, places it
                    
                    if(goalHasPlaced == False):
                        #5% chance to spawn a goa
                        if(i != 0 and j != 0):
                            if(chance >= 95):
                                self.board[i][j] = "$"
                                goalHasPlaced = True
                    if(random.randint(1,1000) > 998):
                        self.board[i][j] = "?"
                            
        while enemyCount > 0 or goalHasPlaced == False:     
            #continues randomization for enemies or goals if either or both are not at an adequate amount
            for i in range(0,len(self.board)):
                for j in range(0,len(self.board)):
                    chance = random.randint(0,100)
                    if(self.board[i][j] == 0):
                        if(enemyCount > 0):
                            if(chance <= 15 and chance > 5):
                                self.board[i][j] = "E"
                                enemyCount -= 1
                        if(goalHasPlaced == False):
                            if(chance >= 95):
                                self.board[i][j] = "$"
                                goalHasPlaced = True
        
            
            

        
