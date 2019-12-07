import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counterDict = collections.Counter(nums)
        counterDict = list(sorted(counterDict.items(), key=lambda lv: lv[1]))
        return (counterDict)[0][0]