class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # temp > stack's current temp
                stackT, stackI = stack.pop()
                res[stackI] = index - stackI
                
            stack.append([temp, index])
            
        return res