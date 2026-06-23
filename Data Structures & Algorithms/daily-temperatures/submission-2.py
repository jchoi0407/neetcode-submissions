class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, e in enumerate(temperatures):
            while stack and e > temperatures[stack[-1]]:
                popped = stack.pop()
                ans[popped] = i - popped
            
            stack.append(i)
        
        return ans