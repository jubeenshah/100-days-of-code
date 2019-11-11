def minimumAbsoluteDifference3(arr):
    if len(arr) <= 100:
        minimum = float('inf')
        for i in arr:
            for j in arr:
                if i != j:
                    tempMin = abs(i - j)
                    #print(tempMin)
                    if tempMin < minimum:
                        minimum = tempMin
        return(minimum)
    else:
        diffs = []
        arr.sort()
        for i in range(len(arr)-1):
            diffs.append(abs(arr[i]-arr[i+1]))
        return min(diffs)
minimumAbsoluteDifference3([1, -3, 71, 68, 17])