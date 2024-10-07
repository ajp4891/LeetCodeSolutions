class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]

        for sell in prices:
            if sell < buy:
                buy = sell
            
            if sell - buy > prof:
                prof = sell - buy

        return prof