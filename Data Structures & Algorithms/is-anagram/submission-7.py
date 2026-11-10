class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1
        
        for j in t:
            if j in tMap:
                tMap[j] += 1
            else: 
                tMap[j] = 1
        
        if sMap == tMap:
            return True 
        else: 
            return False