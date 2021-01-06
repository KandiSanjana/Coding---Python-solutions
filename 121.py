class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        low = 9999
        profit = 0
        
        for price in prices:
            if price<low:
                low = price
            else:
                profit = max(price - low, profit)
        return profit
        
