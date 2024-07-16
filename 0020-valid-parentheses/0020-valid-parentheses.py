class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for para in s:
            if para == '(' or para == '{' or para == '[':
                stack.append(para)
            elif stack and para == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and para == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and para == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False 
        
        return len(stack) == 0