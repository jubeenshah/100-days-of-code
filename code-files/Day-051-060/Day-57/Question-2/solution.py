def missingNumber(nums) -> int:
    numberMissing = 0
    nums.sort()
    for eachNum in nums:
        if numberMissing == eachNum:
            numberMissing += 1
        else:
            return numberMissing
    return numberMissing
missingNumber([0])