
#Code_challenge13.py
print("+++++++++++++++++++++")
print("ODD NUMBER SELECTION, press the  0 to stop the loop")
print("+++++++++++++++++++++")
name = input("Enter your name-->:")

S = 0
O = " "
T = True
while T  == "True":
    num = eval(input("Guess a number from Odd number ")) 
    if num %  2 == 1:
        S += num 
        O += (num) + " "
        print(" # ODD NUMBER DETECTED.")
        continue
    elif num == 0:
        print("# THE LOOP HAS BEEN COMPLETED")
        break
else:
     if num % 2 == 0:
                print("# EVEN NUMBER DETECTED")
               else:
                print("Invalid number ")
          continue
print(f" Hi {name} , the sum of all odd numbers in {S} ")
print(f"# ODD NUMBERS includes the ff :>{O}")

