class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur = ans = 0
        for i in range(len(gain)):
            cur += gain[i]
            ans = max(ans, cur)
        
        return ans
