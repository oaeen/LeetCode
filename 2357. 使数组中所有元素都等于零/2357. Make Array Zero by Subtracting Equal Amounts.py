class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        每次操作均会使 nums 数组中 最小的元素非0元素变为0
        因此只需要求出数组中不同的非0元素的个数即可
        """
        return len(set(nums) - {0})
