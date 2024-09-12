class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
            
        for value in dict.values():
            if value > 1:
                return True
        return False