def pairs(k, nums):
    i,j,numPairs = 0, 1, 0
    nums.sort()
    while j < len(nums):
        difference = nums[j] - nums[i]
        if difference > k:
            i += 1
        if difference < k:
            j += 1
        if difference == k:
            numPairs += 1
            j += 1
    return numPairs
    

pairs(2, nums = list(map(int, input().rstrip().split())))