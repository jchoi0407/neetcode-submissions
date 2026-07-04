class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = 0
        for p in piles:
            if p > maxRate:
                maxRate = p

         
        while minRate != maxRate:
            totalHr = 0
            midRate = (minRate + maxRate) // 2
            for b in piles:
                if (b % midRate) == 0:
                    totalHr += b / midRate
                else:
                    totalHr += (b // midRate) + 1

            if totalHr > h:
                minRate = midRate + 1
            elif totalHr <= h:
                maxRate = midRate


        return minRate
