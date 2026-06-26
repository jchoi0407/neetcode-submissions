class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        end = 0
        maxLen = 0
        while end < len(s):
            if not s[end] in seen:
                seen.add(s[end])
                maxLen = max(maxLen, len(seen))
                end += 1
            else: 
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1
        
        return maxLen

                

