/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
   public:
    int climbStairs(int n) {
        n++;
        double root5 = pow(5, 0.5);
        double result =
            1 / root5 * (pow((1 + root5) / 2, n) - pow((1 - root5) / 2, n));
        return (int)(result);
    }
};
// @lc code=end
