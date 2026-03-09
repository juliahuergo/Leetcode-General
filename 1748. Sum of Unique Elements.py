class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        cur = 0

        for num in nums:
            if num not in seen:
                seen[num] = True #True if it is the first encounter
                cur += num
            elif seen[num]:
                seen[num] = False
                cur -= num
            
        return cur
