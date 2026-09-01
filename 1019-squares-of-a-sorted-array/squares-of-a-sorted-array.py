class Solution(object):
    def sortedSquares(self, nums):
        nums=[a*a for a in nums]
        return sorted(nums)
        