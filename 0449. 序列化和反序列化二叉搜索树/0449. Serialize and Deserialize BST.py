# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，
# 或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
# 编码的字符串应尽可能紧凑。


# 说人话：给你一个二叉搜索树，要求你把它序列化(遍历访问得到)成字符串，然后再反序列化(根据字符串恢复)成二叉搜索树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""

        def preorder(node):
            if not node:
                return []
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        return " ".join(preorder(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        data = [int(x) for x in data.split()]

        def build(pre, inorder):
            if not pre:
                return None

            node = TreeNode(pre[0])
            temp = inorder.index(node.val)
            node.left = build(pre[1 : temp + 1], inorder[:temp])
            node.right = build(pre[temp + 1 :], inorder[temp + 1 :])

            return node

        return build(data, sorted(data))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
