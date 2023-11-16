class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length, current_length = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > threshold:
                current_length = 0
            elif i == len(nums) - 1 or nums[i] % 2 != nums[i + 1] % 2:
                current_length += 1
            else:
                current_length = 1

            if nums[i] % 2 == 0:
                max_length = max(max_length, current_length)

        return max_length
