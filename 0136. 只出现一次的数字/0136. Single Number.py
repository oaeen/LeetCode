from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 使用 reduce 依次对列表中的元素进行异或运算
        # 异或运算的特点是：相同为 0，不同为 1
        # 0 ^ x = x
        # x ^ x = 0
        # 所以，对列表中的所有元素进行异或运算，最后的结果就是只出现一次的元素
        return reduce(lambda x, y: x ^ y, nums)
