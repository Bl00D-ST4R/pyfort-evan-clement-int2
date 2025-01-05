# import pyxel as pyx (pour plus tard pas toucher)
import random as rd #self explanatory

class Morpion : #Creating an object Class Tic_tac_toe for easier structure
    '''
    As every function (called method in an object) displayed here
    (except the last one that isn't in the class) is a method of the class
    Morpion, they take for argument self, meaning that they share everything
    created in this class (method, variables, etc...)
    '''

    #Initialazing the object
    def __init__(self):
        #The matrix for the grid
        self.grid=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]

    #Getter -> self explanatory
    def get_grid(self):
        return self.grid

    #Setter -> to modify the grid with s (symbol) at coordinates (row,col)
    def set_grid(self,row,col,s):
        self.grid[row][col]=s

    #Display an interface with the grid
    def display_grid(self):
        l=self.get_grid()
        line=" |---|---|---|" #Lines
        sep=" | " #Separator between grid values
        print(line)
        #Double for loop to assemble everything then display the grid
        for e in l:
            print(sep,end="")
            for i in range(3) :
                if i!=2 :
                    print(e[i]+sep,end="")
                else :
                    print(e[i]+sep)
            print(line)

    #Check if s symbol won, return True or False
    def check_victory(self,s:str)->bool:
        l=self.get_grid()
        '''
        First we check lines
        Double for loop with counter that changes every row and counts if
        every element in the row is the same if yes return true
        '''
        for e in l:
            c=0
            for e2 in e :
                if e2 == s :
                    c+=1
            if c==3 :
                return True
        '''
        Then the columns
        Double for loop with counter that changes every column and counts if
        every element in the column is the same if yes return true
        '''
        for i in range(3):
            c=0
            for e in l :
                if e[i]==s:
                    c+=1
            if c==3 :
                return True
        #Then it checks both diagnonal with coordinates -> no need for loop
        if l[0][0]== s and l[1][1] == s and l[2][2]== s :
            return True
        if l[0][2]== s and l[1][1] == s and l[2][0]== s :
            return True
        #Return false if no victory
        return False

    #I merged master_move and master_turn into 1 function to simplify
    def master_play(self):
        l=self.get_grid()
        #Check if master can win
        #Double for loop to check every case of the grid
        for e in range(3) :
            for f in range(3) :
                #Now if the case is empty it plays the move
                if l[e][f] == " ":
                    self.set_grid(e,f,"O")
                    #THEN it checks if this is a winning move
                    #If not he undoes the move
                    if not self.check_victory("O"):
                        self.set_grid(e,f," ")
                    else :
                    #If it is a winning move well it plays it
                        return
        #Check if has to block the player
        #Double for loop to check every case of the grid
        for e in range(3) :
            for f in range(3) :
                #Now if the case is empty it plays the move BUT with player symbol
                if l[e][f] == " ":
                    self.set_grid(e,f,"X")
                    #If the player can win then he blocks it
                    if self.check_victory("X"):
                        self.set_grid(e,f,"O")
                        return
                    #If the player doesn't win well he just undo
                    else :
                        self.set_grid(e,f," ")
        #Takes center if not taken because powerful position
        if l[1][1]== " " :
            self.set_grid(1,1,"O")
        else: #Random play
            e,f=rd.randint(0,2),rd.randint(0,2)
            while l[e][f] != " " :
                e,f=rd.randint(0,2),rd.randint(0,2)
            self.set_grid(e,f,"O")
        return

    #Player plays
    def player_move(self):
        #Asks for where to play, since lists begin at 0 I added -1
        row=int(input("Choose a row between 1 and 3"))-1
        col=int(input("Choose a column between 1 and 3"))-1
        l=self.get_grid()
        #Check if player chose a valid value -> not already taken case and not out of grid
        bounds=[0,1,2]
        while row not in bounds or col not in bounds :
            row=int(input("You chose a case out of bounds ! Choose a row between 1 and 3"))-1
            col=int(input("Choose a column between 1 and 3"))-1
        while l[row][col] != " " :
            row=int(input("This case is already taken ! Choose a row between 1 and 3"))-1
            col=int(input("Choose a column between 1 and 3"))-1
        self.set_grid(row,col,"X")

    #Checks if there still an empty case in the grid if yes return False
    #Return True at the end if grid is indeed full
    def full_grid(self)->bool:
        for e in self.get_grid() :
            for f in e :
                if f == " " :
                    return False
        return True

    #Use previous methods to see the outcome of the game
    #If game not finished returns false
    def check_result(self):
        if self.check_victory("O") :
            return "The game master has won !"
        elif self.check_victory("X") :
            return "You defeated the game master and won a key !"
        elif self.full_grid():
            return "The game has ended in a draw !"
        return False

'''
So, this is the main function of the game, its outside the class since independant.
It is recursive because it implements a replay functionality, nb is the number of game played.
Further explanations line by line with other comments
'''
def tictactoe_game(nb=None): #Initialize nb=None for first iteration
    if nb == None : #Initialize nb=1 if first iteration
        nb = 1
    #Displays the number of the current game and the empty grid
    print("=================")
    print("[ Game number",nb,"]")
    print("=================")
    ttt=Morpion() #This one creates the object ttt of class Morpion
    ttt.display_grid()
    #Since the game can't have more than 9 turns I did for in range
    for i in range(10):
        #Checks if odd or even turn to see if player or master turn
        #Player always start to give advantage
        if i%2==0 :
            print("Your turn to play !")
            ttt.player_move()
        elif i%1==0 :
            print("The master played this move !")
            ttt.master_play()
        #Display grid at the end of every move
        ttt.display_grid()
        #Checks if game is ended
        #If player won, display winning message and stops the game
        if ttt.check_result() != False :
            if ttt.check_victory("X") :
                print(ttt.check_result())
                return True
            else : #If either master won or stalemate, asks if want to play again
                print(ttt.check_result()) #Display message but don't return
                a = int(input("Do you want to play again ? Press 1 if yes and 2 if no"))
                #Ask if replay
                while a != 1 and a!=2 :
                    a = int(input("Do you want to play again ? Press 1 if yes and 2 if no"))
                #If wants to replay, there goes the recursivity returning the game with number of game +1
                #I do not know yet if I implement a if nb>5 then return ("No more attempts you lost")
                #Could add some difficulty tweaks
                if a == 1 :
                    return tictactoe_game(nb+1)
                #If does not want to replay then ends
                if a == 2 :
                    return False