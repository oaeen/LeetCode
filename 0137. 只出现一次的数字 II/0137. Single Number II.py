# Brute Force
# class Solution:
#     def singleNumber(self, nums):
#         count = defaultdict(int)

#         for x in nums:
#             count[x] += 1

#         for x, freq in count.items():
#             if freq == 1:
#                 return x

#         return -1


# Bit Manipulation
class Solution:
    def singleNumber(self, nums):
        seen_once = seen_twice = 0

        for x in nums:
            seen_once = ~seen_twice & (seen_once ^ x)
            seen_twice = ~seen_once & (seen_twice ^ x)

        return seen_once
