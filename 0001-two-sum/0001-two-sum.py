class Solution(object):
    def twoSum(self, nums, target):
        previousNums = {} # val: index
        result = []
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in previousNums:
                result.append(previousNums[diff])
                result.append(index)
                return result
            previousNums[num] = index
        