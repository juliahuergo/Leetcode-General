class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = 46342

        while left <= right:
            mid = (left+right) // 2
            if x == mid * mid:
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return left - 1
