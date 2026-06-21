class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            "(" : ")", 
            "{" : "}",
            "[" : "]",
        }

        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if not stack or pair[stack[-1]] != char:
                    return False
                else: 
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False

