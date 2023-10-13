class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        
        buy = 0
        sell = 1
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
            
        return maxP