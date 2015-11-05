class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
            
        last = prices[0]
        profit = 0
        for i in prices[1:]:
            if last < i:
                profit = profit + i -last
            last = i
        
        return profit