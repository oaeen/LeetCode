/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
   public:
    ListNode* reverseList(ListNode* head) {
        ListNode* traveler = head;
        ListNode* tmp;
        while (traveler->next != NULL) {
            tmp = traveler;
            traveler->next = tmp;
        }

        return traveler;
    }
};
// @lc code=end
