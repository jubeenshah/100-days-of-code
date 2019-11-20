def getMoneySpent(keyboards, drives, b):
    #drivesAfter = [10-x for x in drives]
    #print(drivesAfter)
    minVal = float('inf')
    for i in drives:
        for j in keyboards:
            #print(i,j,b-i-j)
            if (b-i-j) < minVal and (b-i-j) >= 0:
                minVal = b-i-j
    if minVal == float('inf'):
        return -1
    return (b-minVal)
    pass

getMoneySpent(keyboards, drives, 622830)