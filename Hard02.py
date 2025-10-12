print("Hard2.py")
for J in range(1,6,1):
    for S in range(6,J,-1):
        print(" ",end=" ")
    for O in range(J,0,-1):
        print(" * ",end=" ")
    for A in range(2,J+1,1):
        print(" * ",end=" ")
    print()
  
print("Alternative Diamond")
for J in range(1,6,1):
    for S in range(6,J,-1):
        print(" ",end=" ")
    for O in range(J,0,-1):
        print(" * ",end=" ")
    for A in range(2,J+1,1):
        print(" * ",end=" ")
    print()


for J in range(6,0,-1):
    for S in range(6,J,-1):
        print(" ",end=" ")
    for O in range(J,0,-1):
        print(" * ",end=" ")
    for A in range(2,J+1,1):
        print(" * ",end=" ")
    print()
