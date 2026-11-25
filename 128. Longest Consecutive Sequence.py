class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setNums = set(nums)
        hash_vals = defaultdict(int)

        def compute(val):
            if val in hash_vals:
                return hash_vals[val]
            if val-1 in setNums:
                hash_vals[val] = 1 + compute(val-1)
                return hash_vals[val]
            else:
                return 1
        
        ans = 0
        for num in nums:
            ans = max(ans, compute(num))
        
        return ans
        
