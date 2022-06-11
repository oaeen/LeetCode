# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
# 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
# 返回使 s 单调递增的最小翻转次数。


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        l = [0] * (n + 1)
        r = [0] * (n + 1)
        l[0] = 1 if s[0] == "1" else 0
        r[n - 1] = 1 if s[n - 1] == "0" else 0
        for i in range(1, n):
            l[i] = l[i - 1] + 1 if s[i] == "1" else l[i - 1]
            r[n - i - 1] = r[n - i] + 1 if s[n - i - 1] == "0" else r[n - i]
        print(l)
        print(r)
        ans = r[0]
        for i in range(1, n + 1):
            ans = min(ans, l[i - 1] + r[i])
        return ans


if __name__ == "__main__":
    solution = Solution()
    s = "00011000"
    print(solution.minFlipsMonoIncr(s))
