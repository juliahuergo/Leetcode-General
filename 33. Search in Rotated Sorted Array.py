class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            return -1
        
        
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                k = mid
                break
            elif nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                k = mid - 1
                break
        
        
        #Now we know that the array is left rotated at k
        if target >= nums[0] and target <= nums[k]:
            left = 0
            right = k
        elif len(nums) > k + 1 and target >= nums[k+1] and target <= nums[-1]:
            left = k + 1
            right = len(nums) - 1
        else:
            return -1 
        
        #Now, binary search on the chosen interval
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: #nums[mid] < target
                left = mid + 1
        
        return -1 
            
        
        
            
        
        
                
