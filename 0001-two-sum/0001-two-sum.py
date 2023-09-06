class Solution(object):
    def twoSum(self, nums, target):
        result = []
        
        prev = {} # indx: num
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                result.append(prev[diff])
                result.append(index)
                return result
            prev[num] = index
        