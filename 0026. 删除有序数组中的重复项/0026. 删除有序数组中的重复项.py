class Solution:
    # cheated
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     s = set(nums)
    #     nums[:len(s)] = sorted(s)
    #
    #     return len(s)

    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if (nums[i] != nums[i + 1]):
                nums[x] = nums[i + 1]
                x += 1
        return (x)
