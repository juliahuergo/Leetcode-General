class Solution(object):
    def permute(self, nums):
        
        ans = []
        seen = set()
        cur = []
        n = len(nums)
        
        def backtrack():
            
            if len(cur) == n:
                ans.append(cur[:])
                return 
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    cur.append(num)
                    backtrack()
                    cur.pop()
                    seen.remove(num)
        
        backtrack()
        return ans 
