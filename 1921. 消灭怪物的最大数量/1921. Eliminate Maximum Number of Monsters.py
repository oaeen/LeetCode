from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_times = [d / s for d, s in zip(dist, speed)]
        arrival_times.sort()
        for i, t in enumerate(arrival_times):
            if t <= i:
                return i
        return len(arrival_times)
