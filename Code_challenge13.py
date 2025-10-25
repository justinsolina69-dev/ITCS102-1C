#Code_challenge13.py
print("+++++++++++++++++++++")
print("ODD NUMBER SELECTION\n press the  0 to stop the loop")
print("+++++++++++++++++++++")

name = input("Enter your name :<")

print("ODD NUMBER DETECTOR4")



S = 0
O = " "
Mahal_kopa = True

while Mahal_kopa == True:

    num = eval(input("Enter an odd number: "))



    if num % 2 == 1:  

        print("ODD NUMBER DETECTED")

        S += num
        O += str(num) + " "

        continue

    elif num == 0:

        print("LOOP TERMINATED")

        break

    else:

        if num % 2 == 0:

            print("EVEN NUMBER DETECTED")

        else:

            print("Invalid number / input")

        continue



print(f"Hi! {name}, the sum of all odd numbers is {S}")

print(f"ODD NUMBERS include the ff --> {O}")







