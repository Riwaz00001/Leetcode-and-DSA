class Solution(object):
    @classmethod
    def removeElement(self, nums, val):
        previous=0
        for current in range(len(nums)):
            if nums[current]!=val:
                nums[previous]=nums[current]
                previous+=1
        return previous
Solution.removeElement([3,2,2,3],3)
Solution.removeElement([0,1,2,2,3,0,4,2],2)