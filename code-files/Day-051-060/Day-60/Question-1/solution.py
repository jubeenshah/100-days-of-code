def moveZeroes(nums):
    for number in nums:
        if number == 0:
            try:
                nums.remove(number)
                nums.append(number)
            except:
                continue
        else:
            continue
    return nums

moveZeroes([0,1,2,0,0,0,0,0,0,0,0,0,0,0,3])