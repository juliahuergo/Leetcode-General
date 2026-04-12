class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def valid(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        if image[sr][sc] == color:
            return image
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = [(sr, sc)]
        original = image[sr][sc]
        while queue:
            row, col = queue.pop()
            image[row][col] = color
            
            for x, y in directions:
                new_row, new_col = row + y, col + x
                if valid(new_row, new_col) and image[new_row][new_col] == original:
                    queue.append((new_row, new_col))
        
        return image
