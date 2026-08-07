class Solution(object):
    @classmethod
    def longestCommonPrefix(self, strs):
        prefix=""
        reference=strs[0]
        for pos in range(len(reference)):
            current=reference[pos]
            for s in strs:
                if pos>=len(s) or current!=s[pos]:
                    return prefix
            prefix+=current
        return prefix
print(Solution.longestCommonPrefix(["flower","flow","flight"]))
print(Solution.longestCommonPrefix(["dog","racecar","car"]))
