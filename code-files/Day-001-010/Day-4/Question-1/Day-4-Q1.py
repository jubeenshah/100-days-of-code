def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval

def arrayManipulation2(n, queries):
    initArray = [0] * n
    for a,b,valueToAdd in queries:
        #print(eachQuery)
        initArray[a-1:b] = [valueToAdd + x for x in initArray[a-1:b]] 
    return (max(initArray))

print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
print(arrayManipulation2(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))