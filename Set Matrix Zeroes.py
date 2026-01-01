class Solution(object):
    def setZeroes(self, matrix):
        setRows = set()
        setCols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if(matrix[i][j] == 0):
                    setRows.add(i)
                    setCols.add(j)
        
        for row in setRows:
            matrix[row] = [0] * len(matrix[0])
        
        for col in setCols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
                    
