class Solution(object):
    def missingNumber(self, nums):
        sum_of_nums=0
        n=len(nums)
        for i in nums:
            sum_of_nums+=i
        sum_n=(n*(n+1))//2
        return sum_n-sum_of_nums
        