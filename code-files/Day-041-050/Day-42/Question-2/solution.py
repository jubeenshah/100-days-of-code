import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        default = collections.defaultdict(int)
        for eachElement in nums:
            default[eachElement] += 1
        default = sorted(default.items(), key= lambda lv: lv[1])
        return (default[-1][0])