name = input("Hi whats your name ")
print("Hello " ,name ,"Welcome to my Mangga Recommendation")
Genre = input("Select any genre you want \n (Fantasy, Romance , Horror) : ")
Size = input("Select any Size \n (Short/Medium/Long) : ")
Year = input("Select year you want \n (2000/2005/2010) : ")

#1
if Genre.lower() == "Fantasy":
    print(" \n You selected: ", Genre)
    if Year == "2000":
        print("  I recommend: \n Moonlight ")
    elif Year == "2005":
        print(" I recommend: \n Berserk ")
    elif Year == "2010":
        print(" I recommend: \n Zom100 ")
    else:
        print("  \n Sorry we dont have Fantasy mangga Available ")
    
#2 
if Genre.lower() == "Romance":
    print(" \n You selected: ", Genre)
    if Year == "2000":
        print(" I recommend: \n AttackOnTitan ")
    elif Year == "2005":
        print(" \n I recommend: \n  Cleavates ")
    elif Year == "2010":
        print(" \n I recommend: \n Darkness ")
    else:
        print("  \n Sorry we dont have Romance mangga Available ")
    
#3
if Genre.lower() == "Horror":
    print("You selected: ", Genre)
    if Year == "2000":
        print("I recommend:  \n Highland"  )
    elif Year == "2005":
        print(" I recommend:  \n Promise never land" )
    elif Year == "2010":
        print(" I recommend:  \n Doomsday ")
        else:
            print("  \n Sorry we dont have Horror mangga  Available ")
else:
print("Sorry we dont have Available mangga ")

