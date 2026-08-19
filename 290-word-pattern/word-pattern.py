class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split(" ")
        map_pattern=[]
        map_s=[]
        for i in pattern:
            map_pattern.append(pattern.index(i))
        for i in s:
            map_s.append(s.index(i))
        return map_pattern==map_s