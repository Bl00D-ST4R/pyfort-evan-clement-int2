import random

def factorial(n):

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def math_challenge_factorial():
  print("Factorial challenge has been selected")
  n = random.randint(1, 10)
  print(f"Calculate the factorial of",n,".")
  player_answer = int(input("Enter your answer: "))
  correct_answer = factorial(n)
  if player_answer == correct_answer:
    print("Congratulations! You have won a key!")
    return True
  else:
    print("Incorrect. The correct answer is",correct_answer,".")
    return False
'''
if math_challenge_factorial():
  print("You have successfully completed the challenge!")
else:
  print("Try again!")
'''

#Clément merged the 2 functions in one for equation challenge
def math_challenge_equation():
    print("Equation challenge has been selected")
    a = random. randint(1, 10)
    b = random. randint(1, 10)
    x = (-b)/a
    print("Solve the equation {}x + {} = 0." .format(a, b))
    X = float(input("What is the value of x:"))
    if X == x :
        print("Correct! You win a key."
    )
    else :
        print("Incorrect! The value of x was :", x)


#checks if n number is prime
def is_prime(n):
    c=0
    #by counting the number of divisors
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    #returning if prime or not
    if c== 2 :
        return True
    else :
        return False

def nearest_prime(n):
    #i and j are 2 counters
    i=1
    j=-1
    if is_prime(n):
        return n
    #first check for highest closest prime then lowest closest prime
    #20 iter since its between 10 and 20
    for k in range(20) :
        if is_prime(n+i):
            return n+i
        i+=1
        if is_prime(n+j):
            return n+j
        j-=1

def math_challenge_prime():
    print("Prime number challenge has been selected")
    n=random.randint(10,20)
    print("What is the closest prime number to",n,"?")
    a=int(input())
    if a == nearest_prime(n):
        print("Correct, you win a key !")
        return True
    else :
        print("The answer was",nearest_prime(n))
        return False

def math_challenge():
    challenges=[math_challenge_factorial,
                math_challenge_equation,
                math_challenge_prime]
    chal=challenges[random.randint(0,2)]
    return chal()