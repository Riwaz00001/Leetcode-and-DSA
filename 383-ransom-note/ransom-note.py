class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine)<len(ransomNote):
            return False
        valid={}
        counter_mag=Counter(magazine)
        for i in magazine:
            if i in valid:
                valid[i]+=1
            else:
                valid[i]=1
        for i in ransomNote:
            if i in valid and valid[i]>0:
                valid[i]-=1
            else:
                return False
        return True
