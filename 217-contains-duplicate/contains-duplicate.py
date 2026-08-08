class Solution(object):
    def containsDuplicate(self, nums):
        seen={}
        for i,v in enumerate(nums):
            if v in seen:
                return True
            seen[v]=i
        return False