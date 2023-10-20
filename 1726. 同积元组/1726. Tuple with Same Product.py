from typing import List
from collections import defaultdict


# brute force
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 遍历数组，从中选出四个元素，计算其中两两元素的乘积
        # 统计乘积相同的元组的个数
        pass


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key = nums[i] * nums[j]
                ans += freq[key]
                freq[key] += 1
        # 一个元组有 8 种排列方式
        # [a,b,c,d], [a,b,d,c], [b,a,c,d], [b,a,d,c]
        # [c,d,a,b], [c,d,b,a], [d,c,a,b], [d,c,b,a]
        return 8 * ans
