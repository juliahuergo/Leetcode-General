class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        
        def check(t):
            count = 0
            for i in range(len(time)):
                count += t // time[i]
                if count >= totalTrips: break
            return count >= totalTrips

        
        left = 1 
        right = totalTrips * min(time)
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
