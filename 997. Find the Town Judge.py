class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        indegree = [0] * n
        outdegree = [0] * n
        for x, y in trust:
            outdegree[x-1] += 1
            indegree[y-1] += 1
        
        ans = -1
        for i in range(n):
            if indegree[i] == n-1 and outdegree[i] == 0:
                if ans == -1: #no other town judges have been found
                    ans = i + 1
                else:
                    return -1
        
        return ans 
