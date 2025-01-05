# Créé par ehana, le 04/01/2025 en Python 3.7
def introduction():
    print("Hello player, welcome to Fort Boyard !")
    print("In this game, your goal is to earn 3 keys to unlock a treasure room,")
    print("You earn keys by completing challenges.")
    print("When you unlock the treasure room, you will play a final challenge,")
    print("The final challenge consists of a word you have to guess from riddles.")
    print("Good luck player !")

def compose_equipe():
    number=int(input("How many players ?"))
    list=[1,2,3]
    while number not in list :
        number=int(input("There must be between 1 and 3 players !"))
    leader= False
    equipe=[]
    for i in range(number):
        l="no"
        n=str(input("What is your name ?"))
        p=str(input("What is your profession ?"))
        if leader == False :
            l=str(input("Are you the leader ?")).lower()
            while l != "no" and l!= 'yes' :
                l=str(input("Are you the leader ?")).lower()
        if l=="yes":
            l2="leader"
            leader=True
        else :
            l2="member"
        dict={"Name":n,"Job":p,"Role":l2,"Keys won":0}
        equipe.append(dict)
    if leader==False :
        equipe[0]["Role"]="leader"
    return equipe


def challenges_menu():
    print("Which challenge do you want to play ?")
    print("1 - Math challenge")
    print("2 - Logic challlenge")
    print("3 - Chance challenge")
    print("4 - Pere fouras's riddles")
    c=int(input())
    list=[1,2,3,4]
    while c not in list :
        c=int(input("Please choose a valid challenge"))
    return c-1

def choose_player(team):
    i=0
    for e in team :
        i+=1
        print(i,e["Name"],"(",e["Job"],")","-",e["Role"])
    c=int(input("Choose a player"))
    list=[1,2,3]
    while c not in list :
        c=int(input("Please choose a valid player"))
    return equipe[c-1]

