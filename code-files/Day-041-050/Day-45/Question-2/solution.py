def firstLast(nums,target):
    firstPos, lastPos = -1,-1
    counter = 0
    for i in nums:
        if i == target:
            firstPos = counter
            break
        counter += 1
    counter = len(nums)-1
    for i in nums[::-1]:
        if i == target:
            lastPos = counter
            break
        counter -= 1
    return [firstPos,lastPos]

firstLast([5,7,7,8,8,10],6)