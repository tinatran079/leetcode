class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy low, sell high
        # profit if prices[sell] > prices[buy]
        
        buy = 0
        sell = 1
        maxP = 0
        
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
            
        return maxP