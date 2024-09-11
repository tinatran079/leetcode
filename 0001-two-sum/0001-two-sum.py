class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # given an array of integers, and integer target
        # return indices of 2 #s that add up to target, in an list
        # num1 + num2 = target
        # complement = target - num
        # have a hash map to keep track of num and index
        # use enumerate to access index and number
        # loop through nums
        # calculate complment
        # if complement is in hash map, then we know we found the 2 #'s
        # append the index from hash map and current indx of num
        # if not, add the cur num and index to hash map
        
        res = []
        prev = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prev:
                res.append(prev[complement])
                res.append(index)
            prev[num] = index
            
        return res
            