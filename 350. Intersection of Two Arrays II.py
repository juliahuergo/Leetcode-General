class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        
        lst = []
        for key, val in counts1.items():
            if key in counts2:
                amount = min(val, counts2[key])
                lst.extend([key]*amount)
        
        return lst
