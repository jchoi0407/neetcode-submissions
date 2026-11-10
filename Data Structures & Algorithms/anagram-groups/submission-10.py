class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
    
        for s in strs:
            count = [0] * 26
            for c in s:
                index = (ord(c) - ord('a'))
                count[index] += 1
            
            key = tuple(count)
            
            if key in table:
                table[key].append(s)
            else:
                table[key] = [s]
        
        return list(table.values())
        
                
            

