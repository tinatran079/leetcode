class Solution(object):
    def twoSum(self, nums, target):
        previous_nums = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in previous_nums:
                return [previous_nums[complement], index]
            previous_nums[num] = index
        return []