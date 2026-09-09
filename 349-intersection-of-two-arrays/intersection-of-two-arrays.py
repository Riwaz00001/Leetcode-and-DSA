class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=Counter(nums1)
        result=[]
        counter=[]
        for i in nums2:
            if i in seen:
                counter.append(i)
        occured=Counter(counter)
        for i in occured:
            if occured[i]>=1:
                result.append(i)
        return result
