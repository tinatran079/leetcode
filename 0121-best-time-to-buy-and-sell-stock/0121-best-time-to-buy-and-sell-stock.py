class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #buy low, sell high
        # profit if buy[i] < sell[i]
        
        maxP = float('-inf')
        
        buy = 0
        sell = 1
        
        while sell < len(prices):
            # profit
            if prices[buy] < prices[sell]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return 0 if maxP == float('-inf') else maxP