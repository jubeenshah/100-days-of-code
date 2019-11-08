def miniMaxSum(arr):
    tempMinArray = arr.copy()
    tempMaxArray = arr.copy()
    minSum = 0
    maxSum = 0

    while len(tempMinArray) > 1:
        currentMin = min(tempMinArray)
        minSum += currentMin
        tempMinArray.remove(currentMin)
        #print(tempMinArray,tempMaxArray)
        
    while len(tempMaxArray) > 1:
        currentMax = max(tempMaxArray)
        maxSum += currentMax
        tempMaxArray.remove(currentMax)
        #print(tempMaxArray)
    print(minSum, maxSum)   
    #print(minSum)

    
print(miniMaxSum([1, 2, 3, 4, 5]))
