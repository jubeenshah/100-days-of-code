def diagonalDifference(arr):
    sumDiagonal1 = 0
    sumDiagonal2 = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                print(arr[i][j])
                sumDiagonal1 += arr[i][j]
    arr = arr [::-1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                print(arr[i][j])
                sumDiagonal2 += arr[i][j]
    print(abs(sumDiagonal1-sumDiagonal2))

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))