def twoSum(nums,target):
    hash_map = {}
    for idx, val in enumerate(nums):
        new_val = target - val
        if new_val in hash_map:
            return hash_map[new_val], idx
        else:
            hash_map[val] = idx

twoSum([3,3], 6)