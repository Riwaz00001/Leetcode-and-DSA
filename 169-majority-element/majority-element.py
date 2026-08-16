class Solution(object):
    def majorityElement(self, nums):
        frequency={}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        occurence=0
        for i,v in frequency.items():
            if occurence<v:
                occurence=v
                majority=i
        return majority