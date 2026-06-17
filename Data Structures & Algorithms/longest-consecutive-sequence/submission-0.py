class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set()
        for n in nums:
            temp.add(n)
        # temp = set(nums) >> this also works

        longest = 0
        for n in nums: 
            if (n - 1) in temp:
                continue 
                # can't be starting point
            else: 
                tempCount = 1
                while (n + 1) in temp: 
                    tempCount += 1
                    n += 1 
                if tempCount > longest:
                    longest = tempCount
        
        return longest


                


        
        

        
        