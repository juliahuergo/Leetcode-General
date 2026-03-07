class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        answer = 0
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]

            #minimizing size 
            while curr > target:
                if curr - nums[left] >= target:
                    curr -= nums[left]
                    left += 1
                else:
                    break
            
            if curr >= target:
                answer = min(answer, i - left + 1) if answer != 0 else i - left + 1
            
        return answer 

