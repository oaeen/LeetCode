# 暴力解
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [
                max(grid[i + ii][j + jj] for ii in range(3) for jj in range(3))
                for j in range(len(grid) - 2)
            ]
            for i in range(len(grid) - 2)
        ]
