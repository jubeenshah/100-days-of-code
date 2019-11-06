q = [2, 1, 5, 3, 4]

def countBribes(Q):
    numberOfBribes = 0
    Q = [val-1 for val in Q]
    print(Q)
    for currentIndex, val in enumerate(Q):
        print(currentIndex,val)
        if val - currentIndex > 2:
            print("Too chaotic",val)
            return
        for j in range(max(val-1,0),currentIndex):
            if Q[j] > val:
                numberOfBribes += 1
    print(numberOfBribes)
countBribes(q)