class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left > right
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit


            
