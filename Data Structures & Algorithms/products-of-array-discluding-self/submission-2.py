class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        ans = [1] * len(nums)

        product = 1
        for i in range(0, len(nums)):       
            if (i-1) < 0:
                continue
            else:
                product *= nums[i - 1]
                ans[i] *= product
        
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            if (j + 1) >= len(nums):
                continue
            else: 
                product *= nums[j + 1]
                ans[j] *= product
        
        return ans

