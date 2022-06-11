# 给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。
# 通过从 s 中删除 0 个或多个字符来获得子序列。
# 如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。
# 如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。
# 注意：
# 结果可能很大，你需要对 10^9 + 7 取模 。

# 思路1 得到所有的子序列, 然后判断是否回文, 计算量大, 排除
# 思路2 动态规划
#       1. 当前字符串s 首尾字符相同，则count(s) = 2*count(s[1:-1])+2
#       2. 当前字符串s 首尾字符不相同，则count(s) = count(s[1:])+count(s[:-1])-count(s[1:-1])
#       3. 当前字符串s 长度为1，则count(s) = 1, 长度为0，则count(s) = 0
#       dp[i][j] = dp[i-1][j-1] + dp[i][j-1]


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        if s[0] == s[-1]:
            if s[0] in s[1:-1]:
                return 2 * self.countPalindromicSubsequences(s[1:-1]) + 1
            else:
                return 2 * self.countPalindromicSubsequences(s[1:-1]) + 2
        else:
            return (
                self.countPalindromicSubsequences(s[1:])
                + self.countPalindromicSubsequences(s[:-1])
                - self.countPalindromicSubsequences(s[1:-1])
            )


if __name__ == "__main__":
    solution = Solution()
    s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
    print(solution.countPalindromicSubsequences(s))
