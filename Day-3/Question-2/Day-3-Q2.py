def minimumSwaps(arr):
    print(arr, "Original")
    arr = [val - 1 for val in arr]
    print(arr, "-1")
    arr_dict = {x:i for i,x in enumerate(arr)}
    print(arr_dict)
    result = 0
    print()
    for index, value in enumerate(arr):
        if index != value:
            print(arr,"array")
            print(arr_dict,"array_dict")
            toSwapIndex = arr_dict[index]
            arr[index], arr[toSwapIndex] = index, value
            arr_dict[index] = index
            arr_dict[value] = toSwapIndex
            result += 1
        print()
        
    print(result)
arr = [4,3,1,2]
minimumSwaps(arr)
