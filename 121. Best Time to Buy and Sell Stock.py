class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-min_buy)
            min_buy = min(min_buy, prices[i])
        
        return ans 
