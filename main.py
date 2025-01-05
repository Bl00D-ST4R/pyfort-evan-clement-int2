import logical_challenges as lc
import chance_challenges as cc
import math_challenges as mc
import utility_functions as ut
import final_challenge as fc
import pere_fouras_challenge as pc

def game():
    ut.introduction()
    ut.compose_equipe()
    keys=0
    while keys != 3:
        n=ut.challenges_menu()
        a=None
        player=ut.choose_player()
        if n == 0 :
            a=mc.math_challenge()
        if n == 1 :
            a=lc.tictactoe_game()
        if n == 2 :
            a=cc.chance_challenge()
        if n == 3 :
            a=pc.pere_fouras_riddles()
        if a == True :
            player['Keys won']+=1
            keys += 1
    b=fc.treasure_room()
    if b == False :
        return ("You lost !")
    if b == True :
        return ("You win !")
game()