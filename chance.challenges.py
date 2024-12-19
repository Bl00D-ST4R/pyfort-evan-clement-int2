# Créé par ehana, le 19/12/2024 en Python 3.7
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
