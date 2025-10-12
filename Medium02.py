print("Medium2.py")
print("MULTIPLICATION TABLE MAKER")
number = eval(input("Enter a number: "))
sum = 0

print("Here's the result:")
for J in range(1,11,1):
    print(number,  "x", J,  "=",number * J)
print(" \t")
for S in range(11,21,1):
     print(number,"x" , S, "=",number * S)
print("\t")
for O in range(21,31,1):
     print(number ,  "x", O,  "=", number * O)
print("\t")
for A in range(31,41,1):
     print(number,"x" , A, "=" , number * A)
print("\t")
for B in range(41,51,1):
     print(number ,  "x", B,  "=", number * B)
print("\t")                  

