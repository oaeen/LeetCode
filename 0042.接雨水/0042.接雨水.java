/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        /**
         * ? 暴力思路 ? 按行一遍遍遍历 ? 选择不相邻的两个块，计算中间的雨水，累计求和，然后减去这一层
         */

        // 这个实际算是双指针的解法
        // 跟踪到目前为止已经安全的水位和总水量。
        // 在每个步骤中，处理并丢弃最左侧或最右侧标高的下部标高。
        int left = 0, right = height.length - 1, bucketHeight = 0, rainWater = 0;
        while (left < right) {
            // 根据木桶效应 选取两侧低的一段，并将该端向 左/右 移动
            int lowerHeight = height[left] < height[right] ? height[left++] : height[right--];
            // 较低的一端大于桶的高度bucketHeight，要更新桶的高度到lowerHeight
            bucketHeight = Math.max(bucketHeight, lowerHeight);
            rainWater += bucketHeight - lowerHeight;
        }
        return rainWater;
    }

}
// @lc code=end
