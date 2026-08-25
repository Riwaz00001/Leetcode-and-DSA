class Solution(object):
    def missingMultiple(self, nums, k):
        seen=set(nums)
        current=k
        while current in seen:
            current+=k
        return current