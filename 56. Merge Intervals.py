class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        ans = []
        left, right = intervals[0]

        for i in range(1, len(intervals)):
            x, y = intervals[i]
            if x <= right:
                right = max(right, y)
            else:
                ans.append([left, right])
                left = x
                right = y
        
        ans.append([left, right])
        
        return ans 
