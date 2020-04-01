NUM_LEVEL=2 
for n in range(NUM_LEVEL):
    for m in range(NUM_LEVEL-n): print(" ", end='')
    for o in range(n*2+1):print("*", end='')
    print("")
