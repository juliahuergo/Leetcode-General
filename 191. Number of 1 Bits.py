class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n: #when n == 0 it is False
            n &= n - 1 #removes rightmost set bit
            count += 1
        
        return count
