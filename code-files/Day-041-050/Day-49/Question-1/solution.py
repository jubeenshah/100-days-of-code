def leftRotation(nums,k):
    numsRotated = nums[k:]+nums[:k]
    for each in numsRotated:
        print(each, end=" ")
leftRotation([1,2,3,4,5],4)