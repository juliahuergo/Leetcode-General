class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        ans = float("-inf")
        while left < right:
            ans = max(min(height[left], height[right]) * (right-left), ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans 
