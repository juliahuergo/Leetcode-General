class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1'
        
        def dfs(row, col):
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)
            
        
        seen = set()
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (i, j) not in seen and grid[i][j] == '1':
                    seen.add((i, j))
                    ans += 1
                    dfs(i, j)
        
      
        return ans 
        
