class Solution(object):
    def isPalindrome(self, s):
        new_string=""
        for i in s:
            if i.isalnum():
                new_string+=i.lower()
        original=new_string
        new_string=new_string[::-1]
        if new_string==original:
            return True
        else:
            return False