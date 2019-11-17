def removeVal(nums, val):
    curr = 0
    while curr < len(nums):
        #print(nums[curr], nums)
        if nums[curr] == val:
            del nums[curr]
            curr -= 1
        curr += 1
    print(nums)

removeVal([0,1,2,2,3,0,4,2], 2)