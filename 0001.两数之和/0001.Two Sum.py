class Solution(object):
    def twoSum(self, nums, target):
        d = {}  # create a dictionary
        for index, num in enumerate(nums):
            if target - num in d:  # if the difference is in the dictionary
                return d[target - num], index
            d[num] = index  # store the index of the number in the dictionary
