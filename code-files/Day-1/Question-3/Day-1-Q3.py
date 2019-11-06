def jumpingOnClouds(c):
    numberOfJumps,i = 0, 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i+2] != 1:
            i += 1
        numberOfJumps += 1
        i += 1
        print(c[i:])
    print(numberOfJumps)

jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])