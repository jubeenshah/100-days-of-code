def threeSum(nums: list):
    nums.sort()
    listToReturn = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        partialTarget = 0 - nums[i]
        #print(partialTarget)
        start = i + 1
        end = len(nums) - 1
        while start < end:
            partialSum = nums[start] + nums[end]
            if partialSum == partialTarget:
                listToReturn.append([nums[i],nums[start],nums[end]])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end-1]:
                    end -= 1
                start += 1
                end -= 1
            elif partialSum < partialTarget:
                start += 1
            else:
                end -= 1
    return listToReturn
threeSum([-1, 0, 1, 2, -1, -4])