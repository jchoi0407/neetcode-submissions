class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26

        for e1 in s1:
            index_1 = ord(e1) - ord('a')
            s1_count[index_1] += 1
        
        if len(s1) > len(s2):
            return False
        else:
            start = 0 
            end = start + len(s1)
            while end <= len(s2): 
                for i in range(start, end):
                    index_2 = ord(s2[i]) - ord('a')
                    s2_count[index_2] += 1
                
                if s1_count == s2_count:
                    return True
                else:
                    start += 1
                    end = start + len(s1)
                    s2_count = [0] * 26        
        return False