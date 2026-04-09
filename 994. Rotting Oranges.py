class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] ==1
        
        queue = deque()
        seen = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: #rotten
                    queue.append((i, j, 0)) # (row, col, steps)
                    seen.add((i, j))
                elif grid[i][j] == 1: #fresh
                    fresh.add((i, j))
        
        #Edge case 1: no rotten oranges but there are fresh oranges 
        if len(queue) == 0 and len(fresh) != 0:
            return -1 

        #Edge case 2: no fresh oranges:
        if len(fresh) == 0:
            return 0
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            row, col, steps = queue.popleft()
            
            for x, y in directions:
                new_row, new_col = row+x , col+y
                
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    fresh.remove((new_row, new_col))
                    queue.append((new_row, new_col, steps+1))
                
                if len(fresh) == 0:
                    return steps + 1
        

        return -1
