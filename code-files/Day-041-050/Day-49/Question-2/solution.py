def rob(nums: list) -> int:
    max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
    for cur in nums:
        max_3_house_before, max_2_house_before, adjacent = \
        max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
    return max(max_2_house_before, adjacent)

rob([2,7,9,3,1])