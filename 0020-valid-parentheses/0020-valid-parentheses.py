class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack and char == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and char == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
                
        return len(stack) == 0
        
        