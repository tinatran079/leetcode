class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy low sell high - buy before selling
        buy = 0
        sell = 1
        maxP = float('-inf')
        
        while sell < len(prices):
            # profit?
            if prices[sell] > prices[buy]:
                maxP = max(maxP, prices[sell] - prices[buy])
            else:
                # buying price is greater than selling price
                buy = sell
            sell += 1
            
        return 0 if maxP == float('-inf') else maxP
                
        