class Solution:
    def countPoints(self, rings: str) -> int:
        ring_locations = [set() for _ in range(10)]
        for i in range(len(rings) // 2):
            ring_locations[int(rings[i * 2 + 1])].add(rings[i * 2])
        return sum(len(location) >= 3 for location in ring_locations)
