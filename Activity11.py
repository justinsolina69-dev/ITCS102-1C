temp = eval(input("enter temperature :"))

if temp <= 5:
    print("Mild Cold ")
elif temp >= 5  and temp <= 10: print("Super Cold   Achoooooo!")
elif temp >= 10 and temp <= 15:
    print("Extremely Cold  Ahhhhhhhhhhh! ")
elif temp >= 15 and temp <=20:
    print("DANGER!!!")
else:
    print("invalid temperature")