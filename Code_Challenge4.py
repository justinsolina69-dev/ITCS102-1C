name = input("Hi whats your name ")
print("Hello " ,name ,"Welcome to my Mangga Recommendation")
Genre = input("Select any genre you want \n (Fantasy, Romance , Horror) : ")
Size = input("Select any Size \n (Short/Medium/Long) : ")
Year = input("Select year you want \n (2000/2005/2010) : ")

#1
if Genre.lower() == "Fantasy":
    if Size.lower() == "Short":
        print(" \n You selected: ", Size )
        if Year == "2000":
            print("  I recommend: \n Moonlight ")
            if Year == "2005":
                print(" I recommend: \n Berserk ")
                if Year == "2010":
                    print(" I recommend: \n Zom100 ")
                 
               
    
#2 
if Genre.lower() == "Romance":
     if Size.lower() == "medium":
         print(" \n You selected: ", Genre)
         if Year == "2000":
             print(" I recommend: \n AttackOnTitan ")
             if Year == "2005":
                 print(" \n I recommend: \n  Cleavates")
                 if Year == "2010":
                     print(" \n I recommend: \n Darkness ")
              
    
#3
if Genre.lower() == "Horror":
     if Size.lower() == "long":
         print("You selected: ", Genre)
         if Year == "2000":
             print("I recommend:  \n Highland"  )
             if Year == "2005":
                 print(" I recommend:  \n Promise never land")
                 if Year == "2010":
                     print(" I recommend:  \n Doomsday ")
else:
    print("Sorry we dont have Available mangga ")

