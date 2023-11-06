"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        """
        层序遍历，每层的最后一个节点的next为None，插入'#' 作为层的分隔符
        输入：root = [1,2,3,4,5,None,7]
        输出：[1,#,2,3,#,4,5,7,#]
        """
        if not root:
            return root
        queue = [root, "#"]
        while queue:
            node = queue.pop(0)
            if node == "#":
                if queue:
                    queue.append("#")
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node.next = queue[0] if queue[0] != "#" else None
        return root


if __name__ == "__main__":
    root = [1, 2, 3, 4, 5, None, 7]
    solution = Solution()
    solution.connect(root)
