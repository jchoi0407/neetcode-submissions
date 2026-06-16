class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i in range(0, len(nums)):
            if nums[i] in sumMap:
                return [sumMap[nums[i]], i]
            else: 
                # add current target - nums[i] as key and i as value
                sumMap[target - nums[i]] = i
        