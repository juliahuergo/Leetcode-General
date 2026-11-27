By binary search:
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        
        left = 0
        right = citations[-1]

        def numPapers(val):
            cont = 0
            for num in citations:
                if num >= val:
                    cont += 1
            return cont         
               
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            num = numPapers(mid)
            if num < mid:
                right = mid - 1
            elif num > mid:
                ans = max(ans, mid)
                left = mid + 1
            else:
                return mid
        
        return ans

By counting sort:
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        counts = [0] * (len(citations)+1)

        for num in citations:
            if num > len(citations):
                counts[len(citations)] += 1
            else:
                counts[num] += 1
        
        higher = 0
        for i in range(len(counts)-1, -1, -1):
            if counts[i] + higher >= i:
                return i
            else:
                higher += counts[i]
