def compareTriplets(a,b):
    aliceScore = 0
    bobScore = 0
    for i,j in zip(a,b):
        if i > j:
            aliceScore += 1
        elif i < j:
            bobScore += 1
    print(aliceScore, bobScore)
print(compareTriplets([17,28,30],[99,16,8]))