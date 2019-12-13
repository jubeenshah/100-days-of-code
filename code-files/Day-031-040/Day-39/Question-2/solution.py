def rotate(nums: list, k: int):
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]
    
nums = [1,2,3,4,5,6,7,8,9,10]
rotate(nums ,1)
print("Value",nums)