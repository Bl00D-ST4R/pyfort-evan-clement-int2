# Créé par ehana, le 19/12/2024 en Python 3.7
import random

def factorial(n):

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def math_challenge_factorial():

  n = random.randint(1, 10)
  print(f"Calculate the factorial of {n}.")
  player_answer = int(input("Enter your answer: "))
  correct_answer = factorial(n)
  if player_answer == correct_answer:
    print("Congratulations! You have won a key!")
    return True
  else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
    return False

if math_challenge_factorial():
  print("You have successfully completed the challenge!")
else:
  print("Try again!")
