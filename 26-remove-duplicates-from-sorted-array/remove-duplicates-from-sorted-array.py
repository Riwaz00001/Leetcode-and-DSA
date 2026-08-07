class Solution(object):
    @classmethod
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        previous=0
        for current in range(1,len(nums)):
            if nums[current]!=nums[previous]:
                previous+=1
                nums[previous]=nums[current]
        return previous+1
print(Solution.removeDuplicates([1,1,2]))
print(Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))