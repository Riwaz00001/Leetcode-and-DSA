class Solution(object):
    def findTheDifference(self, s, t):
        count_s=Counter(s)
        count_t=Counter(t)
        for i in count_t:
            if count_t[i]>count_s[i]:
                return i
            elif i not in count_s:
                return i