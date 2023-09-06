class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(heights)
        res = [0] * n
        
        for i in range(n -1, -1, -1): # start from back:
            height = heights[i]
            
            visible = 0
            
            while stack and height > stack[-1]:
                visible += 1
                stack.pop()
                
            if stack:
                visible += 1
            
            res[i] = visible
            stack.append(height)
            
        return res