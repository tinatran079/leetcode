class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            # selling is higher than buying
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            # buying is higher than selling:
            else:
                l = r
            r += 1
        
        return max_profit
