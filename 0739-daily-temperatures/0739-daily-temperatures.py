class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for index, temp in enumerate(temperatures):
            # is stack empty, is temp greater than top of stack?
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (index - stackInd)
                
            stack.append([temp, index])
            
        return res
        