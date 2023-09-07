class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] # temp, index
        result = [0] * len(temperatures)
        
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # pop
                stackTemp, stackIndex = stack.pop()
                # update result
                result[stackIndex] = index - stackIndex
                
            stack.append([temp, index])
            
        return result