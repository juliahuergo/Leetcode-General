class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1) #O(n)
        nums2 = set(nums2)

        return list(nums1&nums2)
