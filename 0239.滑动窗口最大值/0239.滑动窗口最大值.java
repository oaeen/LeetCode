/*
 * @lc app=leetcode.cn id=239 lang=java
 *
 * [239] 滑动窗口最大值
 * 使用双端队列来求解
 */

// @lc code=start
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) {
            return nums;
        }
        int[] result = new int[n - k + 1];

        // 使用双端队列来求解，队列中存储数组的下标
        LinkedList<Integer> deque = new LinkedList<>();

        // 遍历整个数组。在每一步处理双向队列
        // 只保留当前滑动窗口中有的元素的索引
        // 移除比当前元素小的所有元素，它们不可能是最大的
        // 将当前元素添加到双向队列中
        for (int i = 0; i < n; i++) {
            //如果队列非空 且 队列头元素 在 滑动窗口的头元素 之前
            // 将其删除
            if (!deque.isEmpty() && deque.peek() < i - k + 1) {
                deque.poll();
            }
            // 如果列表非空 且 遍历到的 第i个元素值 比 队列最后一个元素值大
            // 则将队尾元素删除
            // remove smaller numbers in k range as they are useless
            while (!deque.isEmpty() && nums[i] >= nums[deque.peekLast()]) {
                deque.pollLast();
            }
            // 将 i 插入
            deque.offer(i);

            // 将最大值存储
            if (i - k + 1 >= 0) {
                result[i - k + 1] = nums[deque.peek()];
            }
        }
        return result;

    }
}
// @lc code=end

