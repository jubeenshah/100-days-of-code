def search(nums: list, target: int) -> int:
    counter = 0
    for eachElement in nums:
        if eachElement == target:
            return counter
        counter += 1
    return -1 
            

search([4,5,6,7,8,0,1,2,3],2)