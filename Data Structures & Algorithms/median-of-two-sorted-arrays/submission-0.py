class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## brute force solution
        merged = nums1 + nums2
        merged.sort()

        isOdd = len(merged) % 2 == 1
        if isOdd:
            return merged[len(merged) // 2]
        else:
            sum = merged[len(merged) // 2] + merged[(len(merged) // 2) - 1] 
            return sum / 2


                
