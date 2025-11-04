#While loop
name = input("Hi what's your name ?:")
Mahal_moba = True #boolean stopping point

while Mahal_moba == True:
    Sagot = input("Her: Do you still love me? (yes/no):").lower()
    
    if Sagot == "yes":
       print(f"\nHer:Why do you still love me?",name,"")
       break   
      
while Mahal_moba == True:
    Sagot = input("Her:You know I cheated on you right? \n")
    
    if Sagot == "I know":
       print(f"\nHer: Im sorry ...",name," ")
       break   

while Mahal_moba == True:
    Sagot = input("Her: I have a BF now \n and he proposed to me\n")
    
    if Sagot == "That's wonderful":
       print(f"\nHer:Thank you  ...",name," ")
       break               

while Mahal_moba == True:
    Sagot = input("Her: For everything ..\n")
    
    if Sagot == "Im glad":
       print("\nHer: Good bye ...")
       break

while Mahal_moba == True:
    Sagot = input(" ")
    
    if Sagot == "Aishiteru and Sayounara":
       print("\n...")
       break
    else:
      print("\nI wish i knew you wanna be :<")
      break    
