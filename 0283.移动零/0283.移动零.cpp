/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
   public:
    void moveZeroes(vector<int>& test) {
        int j = 0;
        for (int i = 0; i < test.size(); i++) {
            if (test[i] != 0) {
                test[j++] = test[i];
            }
        }
        for (; j < test.size(); j++) {
            test[j] = 0;
        }
    }
};
// @lc code=end
