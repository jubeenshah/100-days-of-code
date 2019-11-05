def binarySearch(nums, target):
    #print(nums,target)
    left = 0
    right = len(nums)-1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot    
        if target > nums[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums, target))
