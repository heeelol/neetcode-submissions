class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        currP = 0

        while r < len(prices):
            if prices[l] > prices[r]: 
                l = r
            
            currP = prices[r] - prices[l]
            
            if currP > maxP:
                maxP = currP

            r += 1

        return maxP
