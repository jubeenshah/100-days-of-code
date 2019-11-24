import collections
def climbingLeaderboard(scores, alice):
    rankDict = collections.Counter(scores)
    #print(rankDict)
    #for index, value in enumerate(rankDict):
        #print(index+1,value, rankDict[value])
    stringToReturn = ""
    for aliceScore in alice:
        scores.append(aliceScore)
        rankDict = collections.Counter(scores)
        rankDict = dict(sorted(rankDict.items(),key= lambda lv : lv[0],reverse=True))
        tempList = []
        for i in rankDict.keys():
            tempList.append(i)
        stringToReturn += str(tempList.index(aliceScore)+1)
        #for index, value in enumerate(rankDict):
        #    if value == aliceScore:
        #        print(index+1)
            #print(index+1,value, rankDict[value])
        #print(rankDict)
        
        scores.remove(aliceScore)
    print(stringToReturn)

climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120])