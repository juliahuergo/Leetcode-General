class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total_remaining = sum(nums)

        ordered = [(nums[i], i) for i in range(len(nums))]
        ordered.sort()


        ans = []
        marked = [False] * len(nums)
        for idx, k in queries:
            if not marked[idx]:
                marked[idx] = True
                total_remaining -= nums[idx]
            
            cont = 0
            while cont < k and ordered:
                next_value, next_idx = ordered[0]
                ordered.pop(0)

                if not marked[next_idx]:
                    marked[next_idx] = True
                    total_remaining -= next_value
                    cont += 1                    
                

            ans.append(total_remaining)

        return ans
            
