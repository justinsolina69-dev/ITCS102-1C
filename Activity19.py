for J in range (1,11,1):
  for S in range(10,1,-1):
    print("", end = "")
  for O in range(1,1,1):
    print("*", end = "")
  for A in range(1,1,1):
    print("*", end = "")
print()

for J in range(1,11,1):
  for S in range(1,1,1):
    print("", end = "")
  for O in range(10,1,-1):
    print("*", end = "")
  for A in range(10,J,-1):
    print("*", end = "")
print()
