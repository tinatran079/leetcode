class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        maxP = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                maxP = max(maxP, prices[sell]-prices[buy])
            else:
                buy = sell
                
        return maxP