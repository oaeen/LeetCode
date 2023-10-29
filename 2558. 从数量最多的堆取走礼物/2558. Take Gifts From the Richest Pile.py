import heapq


class Solution:
    """k n logn"""

    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort()
            gifts[-1] = int(math.sqrt(gifts[-1]))
        return sum(gifts)


import heapq


class Solution:
    """k log n"""

    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(max_gift**0.5))
        return -sum(gifts)
