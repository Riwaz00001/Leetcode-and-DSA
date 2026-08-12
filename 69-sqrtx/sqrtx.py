class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        low,high=1,x
        while low<=high:
            mid=(low+high)//2
            if x==mid*mid:
                return mid
            elif x<mid*mid:
                high=mid-1
            else:
                low=mid+1
        return high

        