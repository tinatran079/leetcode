class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buy = 0
        sell = 1
        
        while sell < len(prices):
            if prices[sell] > prices[buy]: # profit
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            else:
                buy = sell # update pointer bc sell is less than buy
            sell += 1
            
        return maxProfit
        