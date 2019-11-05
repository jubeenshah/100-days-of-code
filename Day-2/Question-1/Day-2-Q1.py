arr = [ [-9, -9, -9,  1, 1, 1], 
        [ 0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [ 0,  0,  8,  6, 6, 0],
        [ 0,  0,  0, -2, 0, 0],
        [ 0,  0,  1,  2, 4, 0],]

height = len(arr)
width  = len(arr[0])

def getSum(matrix, row, col):
    currentSum = 0
    currentSum += matrix[row-1][col-1] #up-left
    currentSum += matrix[row-1][col-0] #up
    currentSum += matrix[row-1][col+1] #up-right
    currentSum += matrix[row+1][col-1] #down-left
    currentSum += matrix[row+1][col-0] #down
    currentSum += matrix[row+1][col+1] #down-right
    currentSum += matrix[row+0][col+0] #current
    return currentSum
    

maxSum = float("-inf")
for i in range(1,width-1):
    for j in range(1,width-1):
        currentSum = getSum(arr, i, j)
        if currentSum > maxSum:
            maxSum = currentSum
print(maxSum)