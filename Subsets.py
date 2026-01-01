class Solution(object):
    def subsets(self, nums):
        ans = []
        cur = []
        
        def backtrack(idx):
            
            if idx == len(nums):
                ans.append(cur[:])
                return 
            
            
            #NOT ADDING IT
            backtrack(idx+1)
            
            #ADDING IT
            cur.append(nums[idx])
            backtrack(idx+1)
            cur.pop()
            
        
        backtrack(0)
        return ans 
