class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = defaultdict(list)
        for i in range(len(nums)):
            num = nums[i]
            if target - num in hash_map:
                return [hash_map[target-num][0], i]
            hash_map[num].append(i)
         
