class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            # since array is sorted, if the first i is greater than 0, then next elements are all positive, which can't be summed to 0
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:

                tempSum = nums[i] + nums[l] + nums[r]
                if tempSum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
                    r -= 1
                elif tempSum > 0:
                    r -= 1
                else:
                    l += 1
        return ans


