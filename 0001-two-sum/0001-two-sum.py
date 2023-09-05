class Solution(object):
    def twoSum(self, nums, target):
        # nums - array of integrs, target - integer
        # return indices of 2 numbers that they add up to target
        # [2, 7, 11, 15] , target = 9 -> [0,1] 
                                        # 2 + 7 = 9
        
        previous = {} # num: index
        result = []
        
        for index, num in enumerate(nums):
            difference = target - num
            if difference in previous:
                result.append(previous[difference])
                result.append(index)
                return result
            previous[num] = index 
        