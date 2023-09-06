class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        res = [0] * len(heights)
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
                res[stack.pop()] += 1 # increment count of popped person
                
            if stack:
                res[stack[-1]] += 1 # if there is still ppl in front of the cur person, increment
                
            stack.append(i)
            
        return res