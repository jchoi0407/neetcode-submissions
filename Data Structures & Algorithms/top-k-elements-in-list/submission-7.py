class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        table = {}
        for n in nums:
            if n in table: 
                table[n] += 1
            else:
                table[n] = 1
        
        arr = [[] for _ in range(len(nums) + 1)]

        for key in table:
            arr[table[key]].append(key)

        res = []
        for j in range(len(arr) - 1, -1, -1):
            for l, e in enumerate(arr[j]):
                res.append(e)
                if len(res) == k:
                    return res
        
        
