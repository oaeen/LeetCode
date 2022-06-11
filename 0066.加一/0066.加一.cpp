/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
   public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size(); i--; digits[i] = 0)
            if (digits[i]++ < 9) return digits;
        digits[0]++;
        digits.push_back(0);
        return digits;
    }
};
// @lc code=end
