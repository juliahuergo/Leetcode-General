class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ans = [1 for x in range(len(ratings))]

        for i in range(len(ans)):
            left, right = 0, 0 
            if i-1 >= 0:
                left = ans[i-1]
            if i+1 < len(ans):
                right = ans[i+1]
            
            if left and ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1 #needs to be higher than its left neighbour
            if right and ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], right+1)
        
        for i in range(len(ans)-1, -1, -1):
            left, right = 0, 0 
            if i-1 >= 0:
                left = ans[i-1]
            if i+1 < len(ans):
                right = ans[i+1]
            
            if left and ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1 #needs to be higher than its left neighbour
            if right and ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], right+1)
        
        return sum(ans)
