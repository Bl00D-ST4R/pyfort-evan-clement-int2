import random
def shell_game() -> bool:
  shells = ['A', 'B', 'C']
  selected_shell = None
  player_choice = None

  print("Welcome to the Shell Game!")
  print("You have 2 attempts to find the key hidden under one of the shells.")
  print("The shells are labeled A, B, and C.")

  for attempt_number in range(1, 3):
    selected_shell = random.choice(shells)

    print(f"Attempt {attempt_number}:")

    player_choice = input("Choose a shell (A, B, or C): ").upper()

    if player_choice in shells:
      if player_choice == selected_shell:
        print(f"Congratulations! You found the key under shell {selected_shell}.")
        return True
      else:
        print(f"You were unsuccessful in this attempt. The key was under shell {selected_shell}.")
    else:
      print("Invalid choice. Please choose A, B, or C.")

    attempt_number += 1

  print(f"You have lost! The key was under shell {selected_shell}.")
  return False

def roll_dice_game():
    a=None
    b=None
    for attempt_number in range(1, 4):
        #player turn
        print(f"Attempt {attempt_number}:")
        input("Roll the dice by pressing 'Enter' key")
        c,d=random.randint(1,6),random.randint(1,6)
        a=(c,d)
        print(a)
        for e in a :
            if e == 6 :
                print("You rolled a 6 and won a key !")
                return True
        #master turn
        c,d=random.randint(1,6),random.randint(1,6)
        b=(c,d)
        print("Master turn :")
        print(b)
        for e in b :
            if e == 6 :
                print("The master has won the game !")
                return False
        print("No one has won, moving one to the next attempt")
    print("No one has won in three turns, it's a draw !")
    return False

def chance_challenge():
    challenges=[shell_game,
                roll_dice_game]
    chal=challenges[random.randint(0,1)]
    return chal()