def mergeIntervals(givenIntervals):
    returnList = []
    for i in sorted(givenIntervals, key=lambda lv : lv[0]):
        if returnList and i[0] <= returnList[-1][1]:
            returnList[-1][1] = max(returnList[-1][1], i[1])
        else:
            returnList += i,
    return returnList

mergeIntervals([[1,3],[2,6],[8,10],[15,18]])