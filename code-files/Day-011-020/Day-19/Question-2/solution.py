import random
def findRunnersUp(arr:list)->int:
    
    arr.sort()
    print(arr)
    maxArray = []
    counter = 0
    for i in range(len(arr)):
        a = arr.pop()
        if a in maxArray or counter == 0:
            maxArray.append(a)
            counter += 1
        else:
            return a
    return maxArray[0]
        

findRunnersUp([2,2,2,2,2,2,2,2,2,2,2,2,2])