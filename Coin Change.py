class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def dp(i):
            
            if i == 0:
                return 0
            
            if i < 0:
                return -1
            
            if i in memo:
                return memo[i]
            
            ans = float('inf')
            for j in range(len(coins)):
                if dp(i-coins[j]) != -1:
                    ans = min(ans, dp(i-coins[j]) + 1)
            
            memo[i] = ans if ans != float('inf') else -1
            return memo[i]
        
        memo = {}
        
        return dp(amount)
                
            
                
        
        
