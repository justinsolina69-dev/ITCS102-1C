#Code_challenge14.py 
#While loop
# Hanime_Title
name = input(" Welcome my fellow weeb  \nEnter your Character name :\n")

Hanime_list = []

I_love_you = True

while I_love_you == True:

    Hanime_Title= input("Enter any Title.(and type \"exit\" to stop): ").lower()


    if Hanime_Title.lower() == "exit":

        print("You have exited the anime entry program")

        I_love_you = False

        

    else:

        Hanime_list.append(Hanime_Title)

print("Your anime list includes: ")

for Hanime_Title in Hanime_list:

    print(f"-->{Hanime_Title}")

