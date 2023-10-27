class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        def get_max_gap(arr, edge):
            """
            计算数组中最大的间隔，包括从0到第一个元素的间隔和从最后一个元素到edge的间隔。
            使用zip和列表推导式生成间隔大小的数组，然后返回最大值。
            """
            return max(b - a for a, b in zip([0] + arr, arr + [edge]))

        return (get_max_gap(horizontalCuts, h) * get_max_gap(verticalCuts, w)) % (
            10**9 + 7
        )
