class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        values={}
        for i,v in enumerate(nums):
            if v in values and i-values[v]<=k:
                return True
            values[v]=i
        return False