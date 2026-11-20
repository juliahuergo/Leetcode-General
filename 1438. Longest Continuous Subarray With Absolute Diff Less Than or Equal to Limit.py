#With 2 heaps
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_queue = []
        max_queue = []

        ans = left = 0

        for right in range(len(nums)):
            heapq.heappush(min_queue, (nums[right], right))
            heapq.heappush(max_queue, (-nums[right], right))

            while -max_queue[0][0] - min_queue[0][0] > limit:
                left = min(max_queue[0][1], min_queue[0][1]) + 1
            
                while max_queue[0][1] < left:
                    heapq.heappop(max_queue)
                
                while min_queue[0][1] < left:
                    heapq.heappop(min_queue)
            
            ans = max(ans, right-left+1)
    
        return ans

#With 2 (monotonic) deques 
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_deque = deque() #smallest at 0
        max_deque = deque() #biggest at 0

        ans = left = 0

        for right in range(len(nums)):
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                elif nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
    
