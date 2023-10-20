# brute force
# class Solution:
#     def sumOfMultiples(self, n: int) -> int:
#         sum = 0
#         for i in range(1, n + 1):
#             if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
#                 sum += i
#         return sum


# veen diagram
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_divisible_by(d):
            """
            求和公式, 1 + 2 + 3 + ... + n = n * (n + 1) // 2
            """
            m = n // d
            return m * (m + 1) // 2 * d

        # 根据 veen 图, 用容斥原理求解
        return (
            sum_divisible_by(3)
            + sum_divisible_by(5)
            + sum_divisible_by(7)
            - sum_divisible_by(15)
            - sum_divisible_by(21)
            - sum_divisible_by(35)
            + sum_divisible_by(105)
        )
