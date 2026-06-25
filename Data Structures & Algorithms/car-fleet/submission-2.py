class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        stack = [] 

        for p, s in pair:
            remainingHrs = (target - p) / s

            if not stack: 
                stack.append(remainingHrs)
            elif stack[-1] >= remainingHrs:
                continue
            else:
                stack.append(remainingHrs)
            
        return len(stack)
            






