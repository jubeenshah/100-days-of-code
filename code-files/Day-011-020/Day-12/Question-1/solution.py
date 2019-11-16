import collections
def luckBalance(k, contests):
    oneList, minLuck,zeroList=  [], [], []
    zeroListSum = 0
    oneListSum = 0
    for i in contests:
        if i[1] == 1: oneList.append(i)
        else: zeroList.append(i)
    numberOfContestsToWin = len(oneList) - k
    for _ in range(numberOfContestsToWin):
        minLuck.append(min(oneList))
        oneList.remove(min(oneList))
    
    for i in zeroList:
        zeroListSum += i[0]
    #print(zeroListSum)
    for i in oneList:
        oneListSum += i[0]
    #print("oneList:", oneListSum)
    sumToReturn = oneListSum + zeroListSum
    for i in minLuck:
        sumToReturn -= i[0]
        
    #print(sumToReturn)
    return sumToReturn
    
luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])