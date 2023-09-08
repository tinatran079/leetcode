class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy, sell = 0, 1 
        
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else: # no profit, shift the buy ptr to where sell ptr is, the lowest
                buy = sell
            sell += 1 # want to update the Right ptr in both cases
            
        return max_profit
                
            