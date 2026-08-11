class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        result = []

        def backtrack(curr, i):
            
            if len(curr) == k:
                result.append(curr[:])
                return
            
            for j in range(i, n+1):
                if len(curr) + (n+1 - j) >= k:
                    curr.append(j)
                    backtrack(curr, j+1)
                    curr.pop()
        
        backtrack([], 1)
        return result
