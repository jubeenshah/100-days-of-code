from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictOfNums = defaultdict(int)
        for eachNum in nums:
            if dictOfNums[eachNum] == 0:
                dictOfNums[eachNum] += 1
            else:
                return True
        return False
        