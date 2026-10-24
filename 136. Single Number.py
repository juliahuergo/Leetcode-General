class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums) #O(n)
        
        for key, val in counts.items():
            if val == 1:
                return key
