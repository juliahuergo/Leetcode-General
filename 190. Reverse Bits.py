class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        for _ in range(32):
            last = n & 1
            n >>= 1

            ans = (ans << 1) | last
            
        return ans
