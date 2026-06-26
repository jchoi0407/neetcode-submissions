class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        start = 0
        end = 0
        maxLen = 0
        while end < len(s):
            if not s[end] in table:
                table[s[end]] = 1
            else: 
                table[s[end]] += 1

            while (end - start + 1) - max(table.values()) > k:
                table[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)

            end += 1
        return maxLen
            
