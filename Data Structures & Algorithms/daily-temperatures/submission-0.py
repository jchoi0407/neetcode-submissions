class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        for i in range(0, len(temperatures)):
            count = 0
            flag = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count += 1
                    flag = True
                    break
                else:
                    count += 1
            
            if flag == True:
                res.append(count)
            else: 
                res.append(0)
        
        return res
            


