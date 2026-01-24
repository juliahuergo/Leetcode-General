class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def dp(i): #LIS ending in index i
            if i == 0:
                return 1
            
            if i in memo:
                return memo[i]
            
            ans = 1
            for j in range(i):
                if nums[j] < nums[i]: #si se puede incluir
                    ans = max(ans, dp(j)+1)
            
            memo[i] = ans
            return memo[i]
        
        memo = {}
        return max(dp(i) for i in range(len(nums)))
