class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                sell += 1
            else: 
                buy = sell
                sell = buy + 1

        return maxProfit