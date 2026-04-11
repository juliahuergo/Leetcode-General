class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        ans = []
        for i in range(numRows):
            row = []
            for j in range(i+1): #num_row = number of elements in the row 
                if j == 0 or j == i: #first or last element in the row (=1)
                    row.append(1)
                else:
                    row.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(row)
        
        return ans 


