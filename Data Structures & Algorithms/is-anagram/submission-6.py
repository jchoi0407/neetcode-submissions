class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        tTable = {}
        for i in s:
            if i in sTable: 
                sTable[i] += 1
            else: 
                sTable[i] = 1
        
        for j in t:
            if j in tTable: 
                tTable[j] += 1
            else: 
                tTable[j] = 1

        if sTable == tTable:
            return True
        else: 
            return False