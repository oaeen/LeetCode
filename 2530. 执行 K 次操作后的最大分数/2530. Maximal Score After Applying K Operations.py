import heapq
from typing import List
import math


# brute force, TLE
# class Solution:
#     def maxKelements(self, nums: List[int], k: int) -> int:
#         score = 0
#         for _ in range(k):
#             nums.sort(reverse=True)
#             score += nums[0]
#             nums[0] = math.ceil(nums[0] / 3)
#         return score


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]  # 将所有元素取负
        heapq.heapify(nums)  # 将列表转换为堆
        for _ in range(k):
            n = -heapq.heappop(nums)  # 弹出最大元素的负数
            score += n
            val = -math.ceil(n / 3)  # 计算新元素的负数
            heapq.heappush(nums, val)  # 将新元素的负数插入堆中
        return score


if __name__ == "__main__":
    nums = [10, 10, 10, 10, 10]
    k = 5
    print(Solution().maxKelements(nums, k))
