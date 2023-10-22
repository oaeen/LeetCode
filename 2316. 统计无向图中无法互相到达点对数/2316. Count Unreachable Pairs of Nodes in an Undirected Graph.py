class UnionFind:
    def __init__(self, size):
        """
        初始化方法，创建一个大小为size的并查集。
        root数组用于存储每个节点的根节点，rank数组用于存储每个根节点的秩（即集合的大小）。
        """
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node):
        """
        查找方法，用于查找给定节点的根节点。
        如果一个节点的根节点不是它自己，那么就递归地查找它的根节点。
        在查找过程中，还会进行路径压缩，即将查找路径上的所有节点的根节点直接设置为最终的根节点。
        """
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        """
        合并方法，用于合并两个节点所在的集合。
        首先查找两个节点的根节点，如果根节点不同，那么就将秩较小的集合合并到秩较大的集合中。
        如果两个集合的秩相同，那么就随意选择一个集合合并到另一个集合中，并将合并后的集合的秩增加1。
        """
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        主函数，用于计算无法互相到达的节点对的数量。
        首先，使用并查集处理所有的边，将连通的节点合并到同一个集合中。
        然后，统计每个集合的大小，并将大小存储到group_sizes数组中。
        最后，计算无法互相到达的节点对的数量。
        通过遍历group_sizes数组，将每个集合的大小乘以之前所有集合的大小之和，然后将结果累加到答案中
        """
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union(node1 - 1, node2 - 1)
        group_sizes = list(Counter([uf.find(i) for i in range(n)]).values())
        ans = 0
        first_group_size = group_sizes[0]
        for i in range(1, len(group_sizes)):
            ans += first_group_size * group_sizes[i]
            first_group_size += group_sizes[i]
        return ans
