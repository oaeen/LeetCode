class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat:
            return []
        ans = []
        R, C = len(mat), len(mat[0])
        for r in range(R):
            for c in range(C):
                pos = r + c
                if pos >= len(ans):
                    ans.append([])
                ans[pos].append(mat[r][c])
        return [
            val
            for i, row in enumerate(ans)
            for val in (row if i % 2 else reversed(row))
        ]


if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
