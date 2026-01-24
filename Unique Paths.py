class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def dp(row, col):
            if row == col == 0:
                return 1 # 1 way to reach it (doing nothing)
            
            if row in memo and col in memo[row]:
                return memo[row][col]
            
            #recurrence relation
            ans = 0
            
            if row > 0: #UP
                ans = ans + dp(row-1, col)
            
            if col > 0: #LEFT
                ans = ans + dp(row, col-1)
            
            if row not in memo:
                memo[row] = {}
            
            memo[row][col] = ans
            return memo[row][col]
        
        memo = {}
        return dp(m-1, n-1)
