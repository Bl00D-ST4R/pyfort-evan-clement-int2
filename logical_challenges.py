# import pyxel as pyx (pour plus tard pas toucher)
import random as rd

class Morpion :
    def __init__(self):
        self.symbol=["X","O"]
        self.grid=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
    def get_symbol(self):
        return self.symbol

    def get_grid(self):
        return self.grid
    def set_grid(self,row,col,s):
        self.grid[row][col]=s

    def display_grid(self):
        l=self.get_grid()
        line=" |---|---|---|"
        sep=" | "
        print(line)
        for e in l:
            print(sep,end="")
            for i in range(3) :
                if i!=2 :
                    print(e[i]+sep,end="")
                else :
                    print(e[i]+sep)
            print(line)

    def check_victory(self,s:str)->bool:
        l=self.get_grid()
        #First we check lines
        for e in l:
            c=0
            for e2 in e :
                if e2 == s :
                    c+=1
            if c==3 :
                return True
        #Then the columns
        for i in range(3):
            c=0
            for e in l :
                if e[i]==s:
                    c+=1
            if c==3 :
                return True
        #Then the left diagonal
        if l[0][0]== s and l[1][1] == s and l[2][2]== s :
            return True
        #Then the right diagonal
        if l[0][2]== s and l[1][1] == s and l[2][0]== s :
            return True
        #Return false if no victory
        return False

    #I merged master_move and master_turn into 1 function to simplify
    def master_play(self):
        l=self.get_grid()
        #check if master win
        for e in l :
            for f in e :
                if e[f] == " ":
                    self.set_grid(e,f,"O")
                    if not self.check_victory("O"):
                        self.set_grid(e,f," ")
                    else :
                        return
        #check if has to block the player
        for e in l :
            for f in e :
                if e[f] == " ":
                    self.set_grid(e,f,"X")
                    if self.check_victory("X"):
                        self.set_grid(e,f,"O")
                        return
        #random play



tic_tac_toe=Morpion()
#tests
tic_tac_toe.display_grid()
print(tic_tac_toe.check_victory("X"))
print(tic_tac_toe.check_victory("O"))