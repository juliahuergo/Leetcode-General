class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        memo = {}

        def dp(i, holding):
            if len(prices) == i:
                return 0
            
            if (i + 1, holding) not in memo:
                memo[(i + 1, holding)] = dp(i + 1, holding)
            ans = memo[(i + 1, holding)] #skip

            if holding:
                if (i + 1, False) not in memo:
                    memo[(i + 1, False)] = dp(i + 1, False)
                ans = max(ans, prices[i] + memo[(i + 1, False)]) #skip or sell
            else:
                if (i + 1, True) not in memo:
                    memo[(i + 1, True)] = dp(i + 1, True)
                ans = max(ans, -prices[i] + memo[(i + 1, True)]) #skip or buy
            
            return ans 
        
        return dp(0, False)
