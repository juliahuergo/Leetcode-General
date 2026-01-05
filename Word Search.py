class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def inside(row, col):
            return row >= 0 and row < m and col >= 0 and col < n
        
        def backtrack(idx, row, col):
            if idx == len(word):
                return True
            
            #backtracking all neighbours not in seen and which ARE the following letter in the word
            for dy, dx in directions:
                if inside(row+dy, col+dx) and (row+dy, col+dx) not in seen and board[row+dy][col+dx] == word[idx]:
                    seen.add((row+dy, col+dx))
                    if backtrack(idx+1, row+dy, col+dx): return True
                    seen.remove((row+dy, col+dx))
          
            
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
            
        seen = set()
        m = len(board)
        n = len(board[0])
        
        #iterating over the cells that contain the starting letter of the word
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen.add((i, j))
                    if backtrack(1, i, j):
                        return True
                    seen.remove((i,j))
        
        #none found the word
        return False
