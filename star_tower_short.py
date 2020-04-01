NUM_LEVEL=5 
for n in range(NUM_LEVEL):
    for m in range(NUM_LEVEL*2+1):
        if m >= NUM_LEVEL-n and m <= NUM_LEVEL+n:
            print("*", end='')
        else:
            print(" ", end='')
    print("")
