class Solution(object):
    def strStr(self, haystack, needle):
        start=0
        to=len(needle)
        for start in range(len(haystack)):
            to=start+len(needle)
            if len(needle)>len(haystack):
                return -1
            if to>len(haystack):
                return -1
            if needle==haystack[start:to]:
                return start
        return -1
        