class Solution:
    def binary_search(self, potions, success, spell):
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if spell * potions[mid] >= success:
                right = mid - 1
            else:
                left = mid + 1
        return len(potions) - left

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        return [self.binary_search(potions, success, spell) for spell in spells]
