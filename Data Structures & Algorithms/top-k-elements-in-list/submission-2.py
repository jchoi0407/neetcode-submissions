class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        frequent_map = {}
        for n in nums: 
            if n in frequent_map:
                frequent_map[n] += 1
            else: 
                frequent_map[n] = 1
        
        for i in range(k): 
            highest_val = 0
            highest_key = 0
            for e in frequent_map:
                if frequent_map[e] > highest_val:
                    highest_val = frequent_map[e]
                    highest_key = e

            ans.append(highest_key)
            frequent_map.pop(highest_key)
            
        return ans
        

