import json
import random

def load_files(path):
    f=open(path,'r')
    a=json.load(f)
    return a


def pere_fouras_riddles():
    p="./Data/PFRiddles.json"
    l=load_files(p)
    a=random.randint(0,46)
    riddle=l[a]
    print(riddle['question'])
    print('You have 3 attempts !')
    for attempt_number in range(1, 4):
        print("Attempt",attempt_number,":")
        b=str(input()).lower()
        if b== riddle['answer'] :
            print('Your answer is correct ! You win a key')
            return True
        else :
            print('Your answer is not correct')
    print('You lost, the answer was :',riddle['answer'],"!" )
    return False
