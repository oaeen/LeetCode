class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        tmp = "01"
        while tmp in s:
            tmp = "0" + tmp + "1"
        return len(tmp) - 2
