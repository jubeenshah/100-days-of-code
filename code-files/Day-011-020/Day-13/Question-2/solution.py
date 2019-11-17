def removeDuplicates(arr):
    i = 0
    while i < len(arr) -1:
        #print(arr, i, arr[i])
        if arr[i] == arr[i+1]:
            del arr[i+1]
            i -=1
        i += 1
    return len(arr)
removeDuplicates([0,0,1,1,1,2,2,3,3,4])