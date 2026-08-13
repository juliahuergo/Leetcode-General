class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def inBoard(i, j):
            return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

        directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        def numNeighbours(i, j):
            count = 0
            for dy, dx in directions:
                y, x = i+dy, j+dx
                if inBoard(y, x):
                    count += board[y][x]
            return count

        neighbours = [[] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                neighbours[i].append(numNeighbours(i, j))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    if neighbours[i][j] < 2 or neighbours[i][j] > 3:
                        board[i][j] = 0
                elif neighbours[i][j] == 3:
                    board[i][j] = 1
        
        return board
