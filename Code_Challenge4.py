print("Welcome to my Mangga Recommendation")
print("Choode wisely")

genre = input("Select any genre you want\n (fantasy ,romance,horror) : ").lower()
year = input("Select year you want\n (2000s ,2005s,2010s) : ").lower()

if genre == "fantasy":
        if year == "2000s":
            print("I recommend: Moonlight ")
        elif year == "2005s":
            print(" I recommend: Berserk")
        elif year == "2010s":
            print(" I recommend: Zom100")
        else:
            print(" no fantasy  recommendation available ")                     
elif genre == "romance":
    if year == "2000s":
        print(" I recommend: AOT")
    elif year == "2005s":
        print(" I recommend: Cleavates")
    elif year == "2010s":
        print(" I recommend: Darkness")
    else:
        print("No romance recommendation available")         
elif genre == "horror":
    if year == "2000s":
        print("I recommend: Highland")
    elif year == "2005s":
        print(" I recommend:  Promiseneverland")
    elif year == "2010s":
        print(" I recommend: Doomsday")
    else:
           print("No horror available")                  
else:
    print("No mangga available")
