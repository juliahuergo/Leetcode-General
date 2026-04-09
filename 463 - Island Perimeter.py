class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

        ans = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    cont = 0
                    for x, y in directions:
                        if valid(row+x, col+y):
                            cont += 1
                        print(cont)
                    ans += (4-cont)
        
        return ans 
                    
