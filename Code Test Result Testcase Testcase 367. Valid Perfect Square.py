class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while(left <= right):
            mid = (left + right) // 2

            prod = mid * mid
            if prod > num:
                right = mid - 1
            elif prod < num:
                left = mid + 1
            else:
                return True
        
        return False
