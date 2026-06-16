class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        ans = []
        
        product = 1
        for i in range(0, len(nums)):       
            if (i-1) < 0:
                continue
            else:
                product *= nums[i - 1]
                pre[i] = product
        
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            if (j + 1) >= len(nums):
                continue
            else: 
                product *= nums[j + 1]
                post[j] = product
        
        for n in range(len(nums)):
            ans.append(pre[n] * post[n])
        
        return ans

