class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # Pairs of (index, height)
        
        for i, h in enumerate(heights):
            start = i
            # If the current height is shorter than the top of the stack,
            # we must pop and calculate the area of those taller bars
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # The popped bar's starting position extends back to 'index'
                start = index
            
            stack.append((start, h))
            
        # Clear out any remaining bars left in the stack
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
            
        return max_area