class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        res = []
        for digit in digits:
            string += str(digit)
        
        nums = int(string) + 1 # 123 + 1 = 124
        
        return [int(num) for num in str(nums)]
        
        
        
        
    # [1, 2, 9]
    # [1, 3, 0]
        