class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] # temp, indx
        res = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # temp of the top of stack
                # get the difference
                stackTemp, stackIndx = stack.pop()
                res[stackIndx] = index - stackIndx
                
            stack.append([temp, index])
            
        return res