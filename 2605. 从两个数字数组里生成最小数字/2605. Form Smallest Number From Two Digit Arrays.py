from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        min1 = min(nums1)
        min2 = min(nums2)
        return min(common) if common else min(min1, min2) * 10 + max(min1, min2)
