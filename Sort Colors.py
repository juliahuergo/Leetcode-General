class Solution(object):
    def sortColors(self, nums):
        counts = Counter(nums)
        lastEdited = 0
        for i in range(counts[0]):
            nums[i] = 0
            lastEdited = lastEdited + 1
        
        lastEditedj = lastEdited 
        for j in range(counts[1]):
            nums[j + lastEdited] = 1
            lastEditedj = lastEditedj + 1
            
        for k in range(counts[2]):
            nums[k + lastEditedj] = 2
            
