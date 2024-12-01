#    № 5,  6
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = (x and (not y)) or (x == z) or (not w)
                if f == False:
                    print(x,y,z,w)