import random

print("Guess a Number")
print("******************")

R_V = random.randint(1,20)
T = 0
G = True

N = input(" Hello! ,What's your name?-->")

while G == True:
    Num = eval(input("Guess a number from 1- 20 :"))
    T += 1
    
    if Num == R_V:
        print("WINNER!")
        break
    else:
        print("Please Guess again.")
        continue

print(f"Hi {N}, Congratulations !, \n your guess is CORRECT!, \nNumber of Tries :{T}")
