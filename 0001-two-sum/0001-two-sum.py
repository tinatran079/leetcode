class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # naive approach
        # input: array of integers and a target integer
        # return: indices of 2 numbers that they add up to targt
        
        # 2 loops. if nums[i] + nums[j] = target, return i & j
        res = []
        
        for i in range(len(nums)):
                            # avoid checking same pair
                            # want unique pairs
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
                
        #[2, 5, 5, 11]
        # i =2, j = 5, 5, 11
        # i = 5, j = 5, 11