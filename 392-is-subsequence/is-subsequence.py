class Solution(object):
    def isSubsequence(self, s, t):
        sub=0
        if len(s)>len(t):
            return False
        if s=="" or s==t:
            return True
        for char in t:
            if sub<=len(s)-1:
                if s[sub]==char:
                    sub+=1
        return sub==len(s)
