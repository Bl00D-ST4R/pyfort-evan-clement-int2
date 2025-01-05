import json
import random

def load_files(path):
    f=open(path,'r')
    a=json.load(f)
    return a

def treasure_room():
    p="./Data/TRClues.json"
    tv_game=load_files(p)
    year=random.choice(list(tv_game['Fort Boyard'].keys()))
    show=random.choice(list(tv_game['Fort Boyard'][str(year)].keys()))
    clues=tv_game['Fort Boyard'][str(year)][show]["Clues"]
    code_word=tv_game['Fort Boyard'][str(year)][show]["CODE-WORD"]
    print(clues[0],clues[1],clues[2])
    for attempt_number in range(1, 4):
        print("Attempt",attempt_number,":")
        answer=str(input("Your answer :"))
        if answer == code_word :
            print("Congratulations ! You won !")
            return True
        print("additional clue:",clues[attempt_number+2])
    print("You lost, the codeword was :",code_word)
    return False