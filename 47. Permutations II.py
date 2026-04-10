class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(curr, seen):
            if len(curr) == len(nums):
                ans.add(tuple(curr[:]))
                return 
            
            for i in range(len(nums)):
                if i not in seen:
                    curr.append(nums[i])
                    seen.add(i)
                    backtrack(curr, seen)
                    seen.remove(i)
                    curr.pop()
            

        ans = set()

        backtrack([], set())
        return list(ans)


