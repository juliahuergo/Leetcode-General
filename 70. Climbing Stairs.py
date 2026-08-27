class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            elif n in memo:
                return memo[n]
            
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        return dp(n)
