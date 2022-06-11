class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            # sum((p + m - 1) / m: trick to ceiling avoid import math
            time = sum((p + m - 1) // m for p in piles)
            if time > h:
                l = m + 1
            else:
                r = m
        return l
