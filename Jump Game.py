class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        def dp(n): 
            memo = [False] * (n)
            memo[-1] = True
            
            for i in range(n-2, -1, -1):
                furthest = min(n-1, i + nums[i])
                for j in range(i+1, furthest+1):
                    if memo[j]: #if the end can be reached from that step, it is possible from current
                        memo[i] = True
                        break
            
            return memo[0]
        
        return dp(len(nums))
