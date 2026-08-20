class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        combination = []
        def dfs(i):
            if sum(combination) == target:
                res.append(combination.copy())
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if sum(combination)  > target:
                    break
                
                combination.append(candidates[j])
                dfs(j + 1)
                combination.pop()
        
        dfs(0)
        return res