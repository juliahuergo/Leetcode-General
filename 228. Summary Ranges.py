class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        left = right = 0
        ans = []
        while right < len(nums):
            curr = [str(nums[left])]
            while right + 1 < len(nums) and nums[right]+1 == nums[right+1]:
                right += 1
            curr.append(str(nums[right]))
            if left != right:
                ans.append("->".join(curr))
            else:
                ans.append(str(nums[left]))
            right += 1
            left = right


        return ans 
