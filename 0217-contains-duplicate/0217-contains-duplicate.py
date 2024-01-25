class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts= {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        for count in counts.values():
            if count > 1:
                return True
        return False