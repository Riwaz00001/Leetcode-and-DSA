class Solution(object):
    @classmethod
    def isPalindrome(cls, x):
        original=x
        if x<0:
            return False
        reverse=0
        while x!=0:
            r=x%10
            reverse=reverse*10+r
            x=x//10
        if reverse==original:
            return True
        else:
            return False
print(Solution.isPalindrome(121))
print(Solution.isPalindrome(-121))
print(Solution.isPalindrome(10))