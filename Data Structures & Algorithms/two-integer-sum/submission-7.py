class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}
        for i, n in enumerate(nums):
            if n in table: 
                return [table[n], i]
            else:
                table[target - n] = i 