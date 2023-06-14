class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            # if an opening bracket, append to stack
            if char in brackets:
                stack.append(char)
            # if stack is nonempty and closing bracket
            # compares closing bracket char with opening bracket
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0