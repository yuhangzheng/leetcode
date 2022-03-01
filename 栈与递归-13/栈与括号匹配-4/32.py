class Solution:
    def longestValidParentheses(self, s: str) -> int:
#         stack = [-1]
#         ret = 0
#         lg = len(s)
#         for i in range(lg):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     ret = max(ret, i - stack[-1])
#         return ret
        # 动态规划
        def comp(strings, order=True):
            ret = 0
            left = right = 0
            for i in strings:
                if i == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    ret = max(ret, left * 2)
                elif order ^ (left > right):
                    left = right = 0
            return ret
        return max(comp(s), comp(s[::-1], False))