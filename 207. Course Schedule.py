class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]s
        :rtype: bool
        """
        visited = 0
        exp_sum = numCourses*(numCourses-1) / 2

        indegree = [0 for i in range(numCourses)]
       
        outgoing = defaultdict(list)
        for a, b in prerequisites:
            outgoing[b].append(a) #edge from b to a
            indegree[a] += 1
        
        queue = deque([])
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        

        while queue:
            node = queue.popleft()
            visited += node
            for edge in outgoing[node]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    queue.append(edge)
        
        return visited == exp_sum
