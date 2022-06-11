# 给定一个由非重叠的轴对齐矩形的数组 rects ，
# 其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角点。
# 设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。
# 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。
# 请注意 ，整数点是具有整数坐标的点。


import bisect
from itertools import accumulate
import random


class Solution:
    def __init__(self, rects):
        w = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.weights = [i / sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        # 使用 bisect 进行有序数组的二分查找
        n_rect = bisect.bisect(self.weights, random.random())
        [ai, bi, xi, yi] = self.rects[n_rect]
        x = random.randint(ai, xi)
        y = random.randint(bi, yi)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
