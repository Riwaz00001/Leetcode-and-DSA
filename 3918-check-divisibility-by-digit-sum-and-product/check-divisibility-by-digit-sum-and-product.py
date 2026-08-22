class Solution(object):
    def checkDivisibility(self, n):
        s=0
        product=1
        original=n
        while n!=0:
            digit=n%10
            s=s+digit
            product*=digit
            n=n//10
        divisor=s+product
        return original%divisor==0