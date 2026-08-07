class Solution(object):
    @classmethod
    def twoSum(cls, nums, target):
        result={}
        for i,v in enumerate(nums):
            subtract=target-v
            if subtract in result:
                results=[result[subtract],i]
                return results
            result[v]=i
print(Solution.twoSum([2,7,11,15],9))
print(Solution.twoSum([3,2,4],6))
print(Solution.twoSum([3,3],6))