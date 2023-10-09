class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack and char == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and char == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
                
        return len(stack) == 0