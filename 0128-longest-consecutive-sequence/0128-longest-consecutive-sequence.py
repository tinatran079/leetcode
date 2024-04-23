class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        longest = 0
        
        for num in nums:
            # check if start of seq
            if (num-1) not in numsSet:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest