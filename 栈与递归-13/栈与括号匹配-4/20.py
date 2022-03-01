class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for b in s:
        #     if b in "([{":
        #         stack.append(b)
        #     elif b == ')':
        #         if len(stack) == 0 or stack[-1] != '(':
        #             return False
        #         stack.pop()
        #     elif b == ']':
        #         if not stack or stack[-1] != '[':
        #             return False
        #         stack.pop()
        #     elif b == '}':
        #         if not stack or stack[-1] != '{':
        #             return False
        #         stack.pop()
        # return not stack

        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack
