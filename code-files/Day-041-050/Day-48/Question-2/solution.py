
def isHappyNumber(n):
    intToStrValue = str(n)
    alreadyVisited = []
    result = 0
    while result != 1:
        result = 0
        for each in intToStrValue:
            #print(each)
            result += int(each)**2
        print(result,alreadyVisited)
        if result not in alreadyVisited:
            alreadyVisited.append(result)
        else:
            return False
        intToStrValue = str(result)
    print(alreadyVisited)
    return True

isHappyNumber(1111111)