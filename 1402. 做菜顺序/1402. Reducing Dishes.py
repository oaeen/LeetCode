class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0
        satisfaction.sort()
        # 只要还有菜可以烹饪，且烹饪下一道菜可以增加总满意度，就继续烹饪
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res
