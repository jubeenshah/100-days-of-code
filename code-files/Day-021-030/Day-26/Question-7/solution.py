def threeSumClosest(nums,target):
    nums.sort()
    print(nums)
    returnVal = []
    difference = sum(nums[:3])
    print(difference)
    for i in range(0, len(nums)):
        j = i + 1
        k = len(nums)-1
        while(j<k):
            sumOfThree = sum((nums[i], nums[j], nums[k]))
            if abs(sumOfThree-target) < abs(difference - target):
                difference = sumOfThree
                print(difference)
            if sumOfThree < target:
                j = j + 1
            elif sumOfThree > target:
                k = k - 1
            else:
                return difference
    return difference
        

threeSumClosest([-1, 2, 9, -4],1)