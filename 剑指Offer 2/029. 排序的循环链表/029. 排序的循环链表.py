"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        insert_node = Node(insertVal)
        # 如果链表为空，则直接构造链表并返回
        if not head:
            insert_node.next = insert_node
            return insert_node
        # 如果链表不为空，则遍历链表，找到插入位置
        node = head
        while node.next != head:
            if node.next.val >= insertVal >= node.val:
                break
            if node.next.val < node.val and (
                node.val <= insertVal or insertVal <= node.next.val
            ):
                break
            node = node.next
        insert_node.next = node.next
        node.next = insert_node
        return head
